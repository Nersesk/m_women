let boxmodal= document.querySelectorAll(".boxmodal")
let researchefooter= document.getElementById("researchfooter")
let modalwindow= document.getElementById("modalwindow")
let closetext = document.getElementById("closetext")
let researches= document.getElementById("researches")
for (let i =0;i<boxmodal.length;i++){
    boxmodal[i].addEventListener("click", modalFunc)
    function modalFunc(){
    modalwindow.style.cssText="transform:translateY(30px);transition:1.5s";
    researchefooter.style.marginTop="1050px";
   researches.style.display="none"
}
}

closetext?.addEventListener("click", modalClose)
function modalClose(){
    modalwindow.style.cssText="transform:translateY(-1030px);transition:1.5s";
    researches.style.cssText="display:grid;align-items:center;justify-content:center"
    modalwindow.style.display="none"
}

let reels = document.getElementById("reels")
let modalreels =document.getElementById("modalreels")
let closereels = document.getElementById("closereels")
let arrowback= document.getElementById("arrowback")

reels?.addEventListener("click", reelsFunc)

function reelsFunc(){
    modalreels.style.cssText="transform:translateY(30px);transition:1.5s";
    modalreels.style.marginTop="-50px"
    modalwindow.style.display="none"

   
}
closereels?.addEventListener("click", reelsClose)
function reelsClose(){
    modalreels.style.cssText="transform:translateY(-730px);transition:1.5s";
  researches.style.display="grid";
  modalreels.style.marginTop="-450px"
   
}

arrowback?.addEventListener("click", backModal)
function backModal(){
    modalreels.style.display="none"
    modalwindow.style.display="block"
}


let images = document.getElementById("images")
let modalimages =document.getElementById("modalimages")
let closeimages = document.getElementById("closeimages")
let arrowbacktwo= document.getElementById("arrowbacktwo")


images?.addEventListener("click", imagesFunc)

function imagesFunc(){
    modalimages.style.cssText="transform:translateY(30px);transition:1.5s";
    researches.style.display="grid"

   
}
closeimages?.addEventListener("click", imagesClose)
function imagesClose(){
    modalimages.style.cssText="transform:translateY(-730px);transition:1.5s"
    modalwindow.style.display="none"
}
arrowbacktwo?.addEventListener("click", backModalTwo)
function backModalTwo(){
    modalimages.style.display="none"
    modalwindow.style.display="block"
}


let files = document.getElementById("files")
let modalfiles =document.getElementById("modalfiles")
let closefiles = document.getElementById("closefiles")
let arrowbackfour= document.getElementById("arrowbackfour")



files?.addEventListener("click", filesFunc)

function filesFunc(){
    modalfiles.style.cssText="transform:translateY(30px);transition:1.5s";
   
}
closefiles?.addEventListener("click",fileClose)
function fileClose(){
    modalfiles.style.cssText="transform:translateY(-730px);transition:1.5s"
    modalwindow.style.display="none"
}
arrowbackfour?.addEventListener("click", backModalFour)
function backModalFour(){
    modalfiles.style.display="none"
    modalwindow.style.display="block"
}
