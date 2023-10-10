const navBtn = document.querySelector(".navbar-toggler")

navBtn.addEventListener("click", () => {
    navBtn.setAttribute("aria-expanded", !navBtn.getAttribute("aria-expanded"))
    document.querySelector(".navbar-collapse").classList.toggle("show")
})

