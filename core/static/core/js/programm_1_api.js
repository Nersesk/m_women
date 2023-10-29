const leng = this.localStorage.getItem("leng");
const lenguage = {
  arm: {},
  eng: {},
};
const lightBoxContainer = document.createElement("div");
const lightBoxContent = document.createElement("div");
const lightBoxImg = document.createElement("img");
const lightBoxPrev = document.createElement("div");
const lightBoxNext = document.createElement("div");

window.addEventListener("load", async function () {
  const id = localStorage.getItem("programId");
  console.log("id", id);
  if (!id) {
    window.location.href = "programm.html";
  } else {
    const programm = await getProgramm(id);
    const article_h2 = this.document.getElementById("article_h2");
    article_h2.innerText = programm.article;
    const programmrow_img = this.document.getElementById("programmrow_img");
    programmrow_img.setAttribute(
      "src",
      `https://xn--29ae4dgic.xn--y9a3aq${programm.main_image}`
    );

    const programmcol_des = this.document.getElementById("programmcol_des");
    const h3 = this.document.createElement("h3");
    h3.innerText = programm.title;
    programmcol_des.appendChild(h3);
    programmcol_des.innerHTML += programm.name;
    const gallery_container = this.document.getElementById("gallery-container");
    programm.program_images.forEach((url, index) => {
      const gallery_item = this.document.createElement("div");
      gallery_item.classList.add("gallery-item");
      gallery_item.setAttribute("data-index", index + 1);
      const img = this.document.createElement("img");
      img.setAttribute("src", `https://xn--29ae4dgic.xn--y9a3aq${url.url}`);
      img.addEventListener("click", () => {
        currentImage(index + 1);
      });
      gallery_item.appendChild(img);
      gallery_container.appendChild(gallery_item);
    });

    lightBoxContainer.classList.add("lightbox");
    lightBoxContent.classList.add("lightbox-content");
    lightBoxPrev.classList.add("fa", "fa-angle-left", "lightbox-prev");
    lightBoxNext.classList.add("fa", "fa-angle-right", "lightbox-next");

    lightBoxContainer.appendChild(lightBoxContent);
    lightBoxContent.appendChild(lightBoxImg);
    lightBoxContent.appendChild(lightBoxPrev);
    lightBoxContent.appendChild(lightBoxNext);

    document.body.appendChild(lightBoxContainer);

    lightBoxPrev.addEventListener("click", prevImage);
    lightBoxNext.addEventListener("click", nextImage);

    lightBoxContainer.addEventListener("click", closeLightBox);
  }
});

async function getProgramm(id) {
  try {
    const response = await fetch(
      `https://տեստէջ.հայ/get_program_detail/${leng}/${id}`,
      {
        method: "GET",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
      }
    );

    if (!response.ok) {
      throw new Error(`Error! status: ${response.status}`);
    }

    const result = await response.json();
    return result;
  } catch (err) {
    console.log(err);
  }
}

let index_img = 1;
function showLightBox(n) {
  const galleryItem = document.getElementsByClassName("gallery-item");
  console.log("index_img", index_img);
  if (n > galleryItem.length) {
    index_img = 1;
  } else if (n < 1) {
    index_img = galleryItem.length;
  }
  console.log(index_img);
  let imageLocation =
    galleryItem[index_img - 1].children[0].getAttribute("src");
  lightBoxImg.setAttribute("src", imageLocation);
}

function currentImage(index) {
  lightBoxContainer.style.display = "flex";
  showLightBox((index_img = index));
}

function slideImage(n) {
  showLightBox((index_img += n));
}
function prevImage() {
  slideImage(-1);
}
function nextImage() {
  slideImage(1);
}
function closeLightBox() {
  if (this === event.target) {
    lightBoxContainer.style.display = "none";
  }
}
