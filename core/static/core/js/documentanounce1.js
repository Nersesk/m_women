const data_index = {
  arm: {
    title_header3: "Հայտարարություն",
    searcher: "Փնտրել",
  },
  eng: {
    title_header3: "Announcement",
    searcher: "Search",
  },
};
window.addEventListener("load", async function (event) {
  let leng = localStorage.getItem("leng");
  if (!leng) {
    localStorage.setItem("leng", "arm");
    leng = "arm";
  }
  const activCir = this.document.getElementById("activCir");
  if (leng === "arm") {
    if (activCir.classList.contains("")) {
      activCir.classList.remove("activ_2");
    }
  } else {
    activCir.classList.add("activ_2");
  }


  const title_header3 = this.document.getElementById("title_header3")
  title_header3.innerText = data_index[`${leng}`].title_header3;

  const searcher = this.document.getElementById("search");
  searcher.setAttribute("placeholder", data_index[`${leng}`].searcher);
});
