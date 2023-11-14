const data_index = {
    arm: {
      title_header8 :"Ծրագիր",
      searcher: "Փնտրել",
      },
    eng: {
        title_header8 :"Program",
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
   

    const title_header8=this.document.getElementById("title_header8")




   
   
  title_header8.innerText=data_index[`${leng}`].title_header8;
  const searcher = this.document.getElementById("search");
  searcher.setAttribute("placeholder", data_index[`${leng}`].searcher);
 
  
  });
  