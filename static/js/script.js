const menuToggle = document.querySelector(".menu-toggle");

const navLinks = document.querySelector(".nav-links");

const icon = menuToggle.querySelector("i");

menuToggle.addEventListener("click", ()=>{

    navLinks.classList.toggle("active");

    if(navLinks.classList.contains("active")){

        icon.classList.remove("fa-bars");

        icon.classList.add("fa-xmark");

        icon.style.color = "white";

    }

    else{

        icon.classList.remove("fa-xmark");

        icon.classList.add("fa-bars");

        icon.style.color = "white";

    }

});

const navbar = document.querySelector(".navbar");

window.addEventListener("scroll", ()=>{

    if(window.scrollY > 80){

        navbar.classList.add("scrolled");

    }

    else{

        navbar.classList.remove("scrolled");

    }

});
const cards = document.querySelectorAll('.destination-card');

cards.forEach((card,index)=>{

    card.style.opacity = '0';
    card.style.transform = 'translateY(40px)';

    setTimeout(()=>{

        card.style.transition = '0.6s ease';
        card.style.opacity = '1';
        card.style.transform = 'translateY(0)';

    },index * 200);
});
const filterButtons =
document.querySelectorAll(
".gallery-filters button"
);

const galleryCards =
document.querySelectorAll(
".gallery-card"
);

filterButtons.forEach(button => {

    button.addEventListener(
    "click", ()=>{

        // REMOVE ACTIVE

        filterButtons.forEach(btn => {

            btn.classList.remove(
            "active-filter"
            );

        });

        // ADD ACTIVE

        button.classList.add(
        "active-filter"
        );

        // GET FILTER

        const filter =
        button.getAttribute(
        "data-filter"
        );

        // FILTER CARDS

        galleryCards.forEach(card => {

            if(
                filter === "all" ||

                card.getAttribute(
                "data-category"
                ) === filter
            ){

                card.style.display =
                "block";

            }

            else{

                card.style.display =
                "none";
            }

        });

    });

});
// ================= EVENTS FILTER =================

const eventFilterButtons =
document.querySelectorAll(".events-tabs button");

const eventCards =
document.querySelectorAll(".events-card");

eventFilterButtons.forEach(button => {

    button.addEventListener("click", () => {

        // REMOVE ACTIVE

        eventFilterButtons.forEach(btn => {

            btn.classList.remove("active");

        });

        // ADD ACTIVE

        button.classList.add("active");

        // FILTER VALUE

        const filter =
        button.getAttribute("data-filter");

        // SHOW HIDE

        eventCards.forEach(card => {

            const category =
            card.getAttribute("data-category");

            if(
                filter === "all" ||
                category === filter
            ){

                card.style.display = "block";

            }

            else{

                card.style.display = "none";

            }

        });

    });

});
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
const searchInput =
document.getElementById("search-input");

const categoryFilter =
document.getElementById("category-filter");

if(searchInput && categoryFilter){

    const rows =
    document.querySelectorAll("tbody tr");

    function filterTable(){

        const search =
        searchInput.value.toLowerCase();

        const category =
        categoryFilter.value;

        rows.forEach(row=>{

            const rowText =
            row.innerText.toLowerCase();

            const rowCategory =
            row.querySelector(".category")
            .innerText.trim();

            const searchMatch =
            rowText.includes(search);

            const categoryMatch =
            category === "all" ||
            rowCategory === category;

            if(searchMatch && categoryMatch){

                row.style.display="";

            }else{

                row.style.display="none";
            }

        });

    }

    searchInput.addEventListener(
        "keyup",
        filterTable
    );

    categoryFilter.addEventListener(
        "change",
        filterTable
    );

}



