window.addEventListener("scroll", () => {

    const navbar = document.querySelector(".navbar");

    if(window.scrollY > 50){
        navbar.style.background = "#0f172a";
    }else{
        navbar.style.background = "rgba(15,23,42,.7)";
    }

});