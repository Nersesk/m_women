window.addEventListener("load", async function (event) {
  const members = this.document.querySelectorAll(".member");
  const show_more_1 = this.document.getElementById("show_more_1");
  let bool = true;
  members.forEach((item, index) => {
    if (index > 5) {
      item.style.display = "none";
    }
  });
  show_more_1.addEventListener("click", () => {
    members.forEach((item, index) => {
      if (bool) {
        item.style.display = "flex";
      } else {
        if (index > 5) {
          item.style.display = "none";
        }
      }
    });
    bool = !bool;
  });
});
