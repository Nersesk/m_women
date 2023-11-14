const data_index = {
    arm: {
        title_header7 :"Արտադրանք",
        
      },
    eng: {
        title_header7:"Product",
        
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
    const title_header7=this.document.getElementById("title_header7")
    




    title_header7.innerText=data_index[`${leng}`].title_header7;
    
 
  
  });
  