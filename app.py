from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask import session
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.secret_key = "mpevents_secret_key"

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mpevents.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ================= USER TABLE =================

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    email = db.Column(db.String(100), unique=True)

    phone = db.Column(db.String(20))

    password = db.Column(db.String(200))

    role = db.Column(db.String(20), default="user")

# ================= CONTACT TABLE =================


class Contact(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    email = db.Column(db.String(100))

    phone = db.Column(db.String(20))

    subject = db.Column(db.String(100))

    message = db.Column(db.Text)


class Booking(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    phone = db.Column(db.String(20))

    email = db.Column(db.String(100))

    event_name = db.Column(db.String(200))

    tickets = db.Column(db.Integer)

class Event(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(200))

    date = db.Column(db.String(50))

    location = db.Column(db.String(100))

    category = db.Column(db.String(50))

    price = db.Column(db.String(50))

    image = db.Column(db.String(200))    

    description = db.Column(db.Text)


# ================= ROUTES =================


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/events")
def events():

    events = Event.query.order_by(
        Event.id.desc()
    ).all()

    return render_template(
        "events.html",
        events=events
)

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        new_message = Contact(

            name=request.form["name"],
            email=request.form["email"],
            phone=request.form["phone"],
            subject=request.form["subject"],
            message=request.form["message"]

        )

        db.session.add(new_message)
        db.session.commit()

        return redirect(url_for("contact"))

    return render_template("contact.html")

    
@app.route("/signin", methods=["GET", "POST"])
def signin():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(
            email=email,
            password=password
        ).first()

        if user:

            session["user_id"] = user.id
            session["user_name"] = user.name

            return redirect(url_for("home"))

        else:

            return redirect(url_for("signin"))

    return render_template("signin.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        password = request.form["password"]

        new_user = User(
            name=name,
            email=email,
            phone=phone,
            password=password
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("signin"))

    return render_template("signup.html")

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))    
    
@app.route("/admin")
def admin():

    if not session.get("user_id"):
        return redirect(url_for("signin"))

    user = User.query.get(session["user_id"])

    if user.role != "admin":
        return redirect(url_for("home"))

    total_users = User.query.count()
    total_events = Event.query.count()
    total_bookings = Booking.query.count()
    revenue = 0
    
    events = Event.query.order_by(
        Event.id.desc()
    ).all()
    bookings = Booking.query.order_by(
        Booking.id.desc()
    ).all()
    users = User.query.order_by(
        User.id.desc()
    ).all()
    messages = Contact.query.order_by(
    Contact.id.desc()
    ).all()

    return render_template(
        "admin.html",
        events=events,
        total_events=total_events,
        total_users=total_users,
        total_bookings=total_bookings,
        revenue=revenue,
        bookings=bookings,
        messages=messages,
        users=users
    )
from werkzeug.security import generate_password_hash

@app.route("/create-admin")
def create_admin():

    admin = User(
        name="Admin",
        email="admin@mpevents.com",
        phone="9999999999",
        password="admin123",
        role="admin"
    )

    db.session.add(admin)
    db.session.commit()

    return "Admin Created Successfully"


@app.route("/booking", methods=["GET","POST"])
def booking():

    if request.method == "POST":
        print(request.form["event_name"])

        new_booking = Booking(

            name=request.form["name"],
            phone=request.form["phone"],
            email=request.form["email"],
            event_name=request.form["event_name"],
            tickets=request.form["tickets"]

        )

        db.session.add(new_booking)
        db.session.commit()

        return redirect(url_for("events"))

    event_name = request.args.get("event")

    return render_template(
        "booking.html",
        event_name=event_name
    )

@app.route("/add-event", methods=["GET", "POST"])
def add_event():

    if request.method == "POST":
        

        image = request.files.get("image")

        print("FILES =", request.files)
        print("IMAGE =", image)
        print("CONTENT TYPE =", request.content_type)
        print("FORM =", request.form)

        filename = ""

        if image and image.filename != "":

            filename = secure_filename(image.filename)

            image.save(
                os.path.join(
                    app.config["UPLOAD_FOLDER"],
                    filename
                )
            )

        new_event = Event(

            name=request.form["name"],
            date=request.form["date"],
            location=request.form["location"],
            category=request.form["category"],
            price=request.form["price"],
            image=filename,
            description=request.form["description"]

        )

        db.session.add(new_event)
        db.session.commit()

        print("EVENT SAVED")
        print(Event.query.count())

        return redirect(url_for("admin"))

    return render_template("add_event.html")

@app.route("/recreate-db")
def recreate_db():
    db.drop_all()
    db.create_all()
    return "Database recreated"   

@app.route("/delete-event/<int:id>")
def delete_event(id):

    event = Event.query.get_or_404(id)

    db.session.delete(event)
    db.session.commit()

    return redirect(url_for("admin"))

@app.route("/edit-event/<int:id>", methods=["GET", "POST"])
def edit_event(id):

    event = Event.query.get_or_404(id)

    if request.method == "POST":

        event.name = request.form["name"]
        event.date = request.form["date"]
        event.location = request.form["location"]
        event.category = request.form["category"]
        event.price = request.form["price"]
        event.description = request.form["description"]

        db.session.commit()

        return redirect(url_for("admin"))

    return render_template(
        "edit_event.html",
        event=event
    )

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)

