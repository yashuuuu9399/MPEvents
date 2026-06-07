const eventsTab = document.getElementById("events-tab");
const bookingsTab = document.getElementById("bookings-tab");
const usersTab = document.getElementById("users-tab");
const messagesTab = document.getElementById("messages-tab");
const analyticsTab = document.getElementById("analytics-tab");

const eventsSection = document.getElementById("events-section");
const bookingsSection = document.getElementById("bookings-section");
const usersSection = document.getElementById("users-section");
const messagesSection = document.getElementById("messages-section");
const analyticsSection = document.getElementById("analytics-section");

function hideAll() {
    eventsSection.style.display = "none";
    bookingsSection.style.display = "none";
    usersSection.style.display = "none";
    messagesSection.style.display = "none";
    analyticsSection.style.display = "none";
}

eventsTab.onclick = () => {
    hideAll();
    eventsSection.style.display = "block";
};

bookingsTab.onclick = () => {
    hideAll();
    bookingsSection.style.display = "block";
};

usersTab.onclick = () => {
    hideAll();
    usersSection.style.display = "block";
};

messagesTab.onclick = () => {
    hideAll();
    messagesSection.style.display = "block";
};

analyticsTab.onclick = () => {
    hideAll();
    analyticsSection.style.display = "block";
};


/* ================= PROFILE MENU ================= */

const profileWrapper = document.querySelector(".profile-wrapper");
const profileIcon = document.querySelector(".profile-icon");

if(profileIcon && profileWrapper){

    profileWrapper.classList.remove("active");

    profileIcon.addEventListener("click", (e) => {

        e.stopPropagation();

        profileWrapper.classList.toggle("active");

    });

    document.addEventListener("click", (e) => {

        if(!profileWrapper.contains(e.target)){
            profileWrapper.classList.remove("active");
        }

    });

}