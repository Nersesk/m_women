const burger_toggle = document.getElementById("burger_toggle");
const burger = document.getElementById("burger");
const aboutus = document.getElementById("aboutus");
const submenu = document.getElementById("submenu");
const burger_menu = document.getElementById("burger_menu");
const cloase = document.getElementById("cloase");
const b_menu = document.getElementById("b_menu");

burger_toggle?.addEventListener("click", () => {
  burger.classList.remove("hide");
  burger.classList.add("show");
  cloase.style.display = "flex";
  b_menu.style.display = "flex";
});
cloase?.addEventListener("click", () => {
  burger.classList.remove("show");
  burger.classList.add("hide");
  cloase.style.display = "none";
  b_menu.style.display = "none";
});

aboutus?.addEventListener("click", () => {
  if (submenu.style.display === "none" || !submenu.style.display) {
    submenu.style.display = "flex";
  } else {
    submenu.style.display = "none";
  }
});



document.addEventListener(
  "DOMContentLoaded",
  function () {
    setTimeout(() => {
      const mess = document.querySelector("body");
      mess?.lastChild?.classList?.add("test_mes");
    }, 4000);
  },
  false
);
