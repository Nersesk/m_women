let countcolone= document.getElementById("countcolone")
let countcoltwo= document.getElementById("countcoltwo")
let countcolthree= document.getElementById("countcolthree")


countcolone.addEventListener("mousemove", myFuncOne)
countcolone.addEventListener("mouseleave", myFuncHoverOne)
countcoltwo.addEventListener("mousemove", myFuncTwo)
countcoltwo.addEventListener("mouseleave", myFuncHoverTwo)
countcolthree.addEventListener("mousemove", myFuncThree)
countcolthree.addEventListener("mouseleave", myFuncHoverThree)
function myFuncOne(){
    countcolone.src="./images/counthover1.svg"
}
function myFuncHoverOne(){
    countcolone.src="./images/count1.svg"
}
function myFuncTwo(){
    countcoltwo.src="./images/counthover2.svg"
}
function myFuncHoverTwo(){
    countcoltwo.src="./images/count2.svg"
}
function myFuncThree(){
    countcolthree.src="./images/counthover3.svg"
}
function myFuncHoverThree(){
    countcolthree.src="./images/count3.svg"
}