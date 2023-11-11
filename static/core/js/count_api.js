const leng = this.localStorage.getItem("leng");
const server_url = main_url();
const lenguage = {
  arm: {
    btn: "ավելին",
  },
  eng: {
    btn: "Show more",
  },
};
window.addEventListener("load", async function () {
  const { product_list, next_page } = await getCount_list(1);
  appenCount_list(product_list, next_page);
});

async function getCount_list(page) {
  try {
    const response = await fetch(
      `${server_url}get_reports/${leng}/${page}`,
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

async function appenCount_list(product_list, next_page) {
  const countrowone = this.document.getElementById("countrowone");
  product_list.forEach((product) => {
    const div = document.createElement("div");
    const img = document.createElement("img");
    const p = document.createElement("p");
    let span_d = product.name.substring(
      product.name.indexOf("2"),
      product.name.length
    );
    p.innerText = product.name.substring(0, product.name.indexOf("2"));
    img.setAttribute("src", `${product.image}`);
    p.innerHTML += `<span >${span_d}</span>`;
    img.setAttribute("alt", "images");
    div.classList.add("countcol");
    div.addEventListener("click", () => {
      let url = `${product.file}`;
      const a = document.createElement("a");
      a.href = url;
      a.download = url;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
    });
    div.appendChild(img);
    div.appendChild(p);
    countrowone.appendChild(div);
  });

  if (next_page !== null) {
    genPartnersMoreButton(next_page);
  }
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
  const { product_list, next_page } = await getCount_list(page);
  appenCount_list(product_list, next_page);
}
