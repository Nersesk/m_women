const leng = this.localStorage.getItem("leng");
const lenguage = {
  arm: {
    btn: "ավելին",
  },
  eng: {
    btn: "Show more",
  },
};
window.addEventListener("load", async function () {
  const { next_page, product_list } = await getProduct_list(1);
  appendProduct_list(product_list, next_page);
});

async function getProduct_list(page) {
  try {
    const response = await fetch(
      `https://տեստէջ.հայ/product_list/${leng}/${page}`,
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
async function getProduct(url) {
  try {
    console.log("urk", url);
    const response = await fetch(`https://տեստէջ.հայ${url}`, {
      method: "GET",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
    });

    if (!response.ok) {
      throw new Error(`Error! status: ${response.status}`);
    }

    const result = await response.json();
    return result;
  } catch (err) {
    console.log(err);
  }
}

async function appendProduct_list(product_list, next_page) {
  const card_section = this.document.getElementById("card_section");
  const svg = ` <svg
                xmlns="http://www.w3.org/2000/svg"
                width="34"
                height="34"
                viewBox="0 0 34 34"
                fill="none"
              >
                <path
                  fill-rule="evenodd"
                  clip-rule="evenodd"
                  d="M17 31.875C20.9451 31.875 24.7286 30.3078 27.5182 27.5182C30.3078 24.7286 31.875 20.9451 31.875 17C31.875 13.0549 30.3078 9.27139 27.5182 6.48179C24.7286 3.69219 20.9451 2.125 17 2.125C13.0549 2.125 9.27139 3.69219 6.48178 6.48179C3.69218 9.27139 2.125 13.0549 2.125 17C2.125 20.9451 3.69218 24.7286 6.48179 27.5182C9.27139 30.3078 13.0549 31.875 17 31.875ZM17 3.0716e-06C21.5087 2.87452e-06 25.8327 1.79107 29.0208 4.97919C32.2089 8.1673 34 12.4913 34 17C34 21.5087 32.2089 25.8327 29.0208 29.0208C25.8327 32.2089 21.5087 34 17 34C12.4913 34 8.1673 32.2089 4.97918 29.0208C1.79107 25.8327 -5.46013e-07 21.5087 -7.43094e-07 17C-9.40174e-07 12.4913 1.79107 8.1673 4.97918 4.97919C8.1673 1.79107 12.4913 3.26868e-06 17 3.0716e-06ZM9.5625 15.9375C9.28071 15.9375 9.01046 16.0494 8.8112 16.2487C8.61194 16.448 8.5 16.7182 8.5 17C8.5 17.2818 8.61194 17.552 8.8112 17.7513C9.01046 17.9506 9.28071 18.0625 9.5625 18.0625L21.8726 18.0625L17.3102 22.6228C17.1107 22.8223 16.9987 23.0929 16.9987 23.375C16.9987 23.6571 17.1107 23.9277 17.3102 24.1273C17.5098 24.3268 17.7803 24.4388 18.0625 24.4388C18.3446 24.4388 18.6152 24.3268 18.8147 24.1273L25.1897 17.7523C25.2887 17.6536 25.3672 17.5363 25.4208 17.4072C25.4743 17.2781 25.5019 17.1398 25.5019 17C25.5019 16.8602 25.4743 16.7219 25.4208 16.5928C25.3672 16.4637 25.2887 16.3464 25.1897 16.2478L18.8147 9.87275C18.6152 9.67324 18.3446 9.56116 18.0625 9.56116C17.7803 9.56116 17.5098 9.67324 17.3102 9.87275C17.1107 10.0723 16.9987 10.3429 16.9987 10.625C16.9987 10.9071 17.1107 11.1777 17.3102 11.3773L21.8726 15.9375L9.5625 15.9375Z"
                  fill="#B3C985"
                />
              </svg>`;
  product_list.forEach((product) => {
    const card_a = document.createElement("div");
    card_a.classList.add("card_a");
    const card_title = document.createElement("div");
    card_title.classList.add("card_title");
    card_title.innerText = product.name;
    const card_main = document.createElement("div");
    card_main.classList.add("card_main");
    const p = document.createElement("p");

    let desc = product.description.replace(/<\/p>/g, "");
    desc = desc.replace(/<p>/g, "");
   
 
    console.log("1", product.description);
    console.log("2", desc);
    p.innerText = desc;
    card_main.appendChild(p);
    card_main.innerHTML += svg;
    card_a.appendChild(card_title);
    card_a.appendChild(card_main);
    card_a.addEventListener("mouseover", () => {
      const elm = document.querySelector(".animation");
      elm?.classList.remove("animation");
      card_a.children[0].classList.add("animation");
      card_a.addEventListener("mouseout", () => {
        elm?.classList.remove("animation");
      });
    });
    card_a.addEventListener("click", () => {
      const modal = document.createElement("div");
      const modal_ash_content = document.createElement("div");
      const cloase = document.createElement("div");
      const tnt = document.createElement("div");
      const photo = document.createElement("div");
      const file = document.createElement("div");
      const modal_main = document.createElement("div");
      const cloaseIcon = document.createElement("i");

      cloaseIcon.classList.add("fa-solid");
      cloaseIcon.classList.add("fa-xmark");
      cloase.classList.add("cloase_modal");

      modal.classList.add("modal_ash");
      modal_ash_content.classList.add("modal_ash_content");
      tnt.classList.add("card_a_2");
      photo.classList.add("card_a_2");
      file.classList.add("card_a_2");
      modal_main.classList.add("modal_main");
      tnt.innerText = "տեսանյութեր";
      photo.innerText = "ֆոտոներ";
      file.innerText = "այլ ֆայլեր";

      cloase.appendChild(cloaseIcon);
      modal_main.appendChild(tnt);
      modal_main.appendChild(photo);
      modal_main.appendChild(file);

      modal_ash_content.appendChild(cloase);
      modal_ash_content.appendChild(modal_main);

      modal.appendChild(modal_ash_content);

      document.body.appendChild(modal);
      cloaseIcon.addEventListener("click", () => {
        modal.remove();
      });
      console.log("product", product);
      tnt.addEventListener("click", () => {
        addModalTnt(product.url);
      });
      photo.addEventListener("click", () => {
        addModalPhoto(product.url);
      });
      file.addEventListener("click", () => {
        addModalfFle(product.url);
      });
    });
    card_section.appendChild(card_a);
  });
  if (next_page !== null) {
    genPartnersMoreButton(next_page);
  }
}

async function addModalTnt(url) {
  const { videos } = await getProduct(url);
  const modal_ash_content = document.querySelector(".modal_ash_content");
  const modal_main = document.querySelector(".modal_main");
  const cloase_modal = document.querySelector(".cloase_modal");
  const beckIcon = document.createElement("div");
  const icon = document.createElement("i");

  beckIcon.classList.add("beckIcon");
  icon.classList.add("fa-solid");
  icon.classList.add("fa-arrow-left-long");
  cloase_modal.classList.add("cloase_modal_step_2");
  beckIcon.appendChild(icon);
  cloase_modal.appendChild(beckIcon);
  modal_main.style.display = "none";
  const modal_main_tnt = document.createElement("div");
  for (let index = 0; index < videos.length; index++) {
    const video = document.createElement("div");
    video.classList.add("video");
    const iframe = document.createElement("iframe");
    console.log(videos[index].url);
    iframe.setAttribute("src", "https://www.youtube.com/watch?v=iBm_AYeQbHE");
    iframe.setAttribute("width", "100%");
    iframe.setAttribute("height", "100%");
    video.appendChild(iframe);
    modal_main_tnt.classList.add("modal_main_tnt");

    modal_main_tnt.appendChild(video);
  }
  modal_ash_content.appendChild(modal_main_tnt);

  beckIcon.addEventListener("click", () => {
    modal_main.style.display = "flex";
    modal_main_tnt.remove();
    beckIcon.remove();
  });
}

async function addModalPhoto(url) {
  const { images } = await getProduct(url);
  const modal_ash_content = document.querySelector(".modal_ash_content");
  const modal_main = document.querySelector(".modal_main");
  const cloase_modal = document.querySelector(".cloase_modal");
  const beckIcon = document.createElement("div");
  const icon = document.createElement("i");

  beckIcon.classList.add("beckIcon");
  icon.classList.add("fa-solid");
  icon.classList.add("fa-arrow-left-long");
  cloase_modal.classList.add("cloase_modal_step_2");
  beckIcon.appendChild(icon);
  cloase_modal.appendChild(beckIcon);
  modal_main.style.display = "none";
  const modal_main_photo = document.createElement("div");
  for (let index = 0; index < images.length; index++) {
    const photo = document.createElement("div");
    photo.classList.add("photo");
    const img = document.createElement("img");
    img.setAttribute(
      "src",
      `https://xn--29ae4dgic.xn--y9a3aq${images[index].url}`
    );
    img.setAttribute("alt", "images");
    img.classList.add("img");
    photo.appendChild(img);
    modal_main_photo.classList.add("modal_main_photo");

    modal_main_photo.appendChild(photo);
  }
  modal_ash_content.appendChild(modal_main_photo);

  beckIcon.addEventListener("click", () => {
    modal_main.style.display = "flex";
    modal_main_photo.remove();
    beckIcon.remove();
  });
}

async function addModalfFle(url) {
  const { files } = await getProduct(url);
  const modal_ash_content = document.querySelector(".modal_ash_content");
  const modal_main = document.querySelector(".modal_main");
  const cloase_modal = document.querySelector(".cloase_modal");
  const beckIcon = document.createElement("div");
  const icon = document.createElement("i");

  beckIcon.classList.add("beckIcon");
  icon.classList.add("fa-solid");
  icon.classList.add("fa-arrow-left-long");
  cloase_modal.classList.add("cloase_modal_step_2");
  beckIcon.appendChild(icon);
  cloase_modal.appendChild(beckIcon);
  modal_main.style.display = "none";
  const modal_main_file = document.createElement("div");
  for (let index = 0; index < files.length; index++) {
    const file = document.createElement("div");
    file.classList.add("file");
    file.innerText = files[index].name;
    file.addEventListener("click", () => {
      let url = `https://xn--29ae4dgic.xn--y9a3aq${files[index].url}`;
      const a = document.createElement("a");
      a.href = url;
      a.download = url.split("/").pop();
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
    });
    modal_main_file.classList.add("modal_main_file");
    modal_main_file.appendChild(file);
  }
  modal_ash_content.appendChild(modal_main_file);

  beckIcon.addEventListener("click", () => {
    modal_main.style.display = "flex";
    modal_main_file.remove();
    beckIcon.remove();
  });
}
function genPartnersMoreButton(next_page) {
  const show_more_1 = this.document.getElementById("show_more_2");
  const button = document.createElement("button");
  button.classList.add("button_global");
  button.innerText = lenguage[`${leng}`].btn;
  button.addEventListener("click", async (event) => {
    button.remove();
    await appendNextProduct_list(next_page);
  });
  show_more_1.appendChild(button);
}

async function appendNextProduct_list(page) {
  const { product_list, next_page } = await getProduct_list(page);
  appendProduct_list(product_list, next_page);
}
