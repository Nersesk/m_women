const lenguage = {
  arm: {
    btn: "Կարդալ ավելին",
    no_data: "Արդյունք չի հայտնաբերվել...",
  },
  eng: {
    btn: "Read more",
    no_data: "No results found...",
  },
};
let clickCount = 0;
const leng = this.localStorage.getItem("leng");
const server_url = main_url();
window.addEventListener("load", async function () {
  const { pages_count } = await getPageCount();
  await pagination(pages_count, 1);
});
async function getPageCount() {
  try {
    const response = await fetch(`${server_url}get_program_pages_count`, {
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

async function getPrograms(page) {
  try {
    const response = await fetch(
      `${server_url}get_programs/${leng}/${page}`,
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
const ulTag = document.querySelector(".pagination ul");
const programmcardrow = document.getElementById("programmcardrow");

async function pagination(totalPages, page, data) {
  let programs_data;

  if (!data) {
    const { programs } = await getPrograms(page);
    programs_data = programs;
  } else {
    programs_data = data;
  }
  throwPrograms(programs_data);
  let liTag = "";
  let beforePage = page - 1;
  let afterPage = page + 1;
  let activeLi = "";

  if (totalPages < 2) {
    liTag += `<li class="num " onClick="pagination(${1}, ${1})"><span>${1}</span></li>`;
  } else {
    if (page > 2) {
      liTag += `        <li class="num " onClick="pagination(${totalPages}, ${1})"><span>1</span></li>
    `;

      if (page > 3) {
        liTag += `        <li class="dots"><span>...</span></li>`;
      }
    }
    if (totalPages > 4) {
      if (page == totalPages) {
        beforePage = beforePage - 2;
      } else if (page == totalPages - 1) {
        beforePage = beforePage - 1;
      }
      if (page == 1) {
        afterPage = afterPage + 2;
      } else if (page == totalPages - 1) {
        afterPage = afterPage + 1;
      }
    }
    for (let pageNum = beforePage; pageNum <= afterPage; pageNum++) {
      if (pageNum > totalPages) {
        continue;
      }
      if (pageNum == 0) {
        continue;
      }
      page == pageNum ? (activeLi = "active") : (activeLi = "");
      liTag += `<li class="num ${activeLi}" onClick="pagination(${totalPages}, ${pageNum})"><span>${pageNum}</span></li>`;
    }
    if (page < totalPages - 1) {
      if (page < totalPages - 2) {
        liTag += `<li class="dots"><span>...</span></li>`;
      }
      liTag += `<li class="num " onClick="pagination(${totalPages}, ${totalPages})"><span>${totalPages}</span></li>`;
    }
  }
  ulTag.innerHTML = liTag;
}

function throwPrograms(programs) {
  programmcardrow.innerHTML = "";
  const modal_content_h2 = document.getElementById("modal_content_h2");

  programs?.forEach((program) => {
    const img = document.createElement("img");
    img.setAttribute("src", `${program.image}`);
    img.setAttribute("alt", "announcecol");
    const front = document.createElement("div");
    front.classList.add("front");
    front.appendChild(img);

   const back_h3 = document.createElement("h3");
    const back_p = document.createElement("p");
    const back = document.createElement("div");
    back.classList.add("back");
    let desc = program.article.replace(/<\/p>/g, "");
    desc = desc.replace(/<p>/g, "");
    desc = desc.substring(0, 398);
    desc += "...";

    back_p.innerHTML = `<p>${desc}</p>`;
    back_h3.innerText = program.name;
    back.appendChild(back_h3);
    back.appendChild(back_p);

   const backgroundtext_p = document.createElement("p");
    const backgroundtext = document.createElement("div");

    backgroundtext_p.innerText = program.title;
    backgroundtext.appendChild(backgroundtext_p);
    backgroundtext.classList.add("backgroundtext");
    const card_container = document.createElement("div");
    card_container.appendChild(front);
    card_container.classList.add("card-container");
    card_container.appendChild(back);
    const cardprogramm = document.createElement("div");
    cardprogramm.classList.add("cardprogramm");

    cardprogramm.appendChild(card_container);
    cardprogramm.appendChild(backgroundtext);
    const userAgent = navigator.userAgent;

    const handler = () => {
      localStorage.setItem("programId", program.id);
      window.location.href = `${server_url}program/${program.id}`;
    }

    if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini|Mobile|mobile|CriOS/i.test(userAgent)) {
      cardprogramm.addEventListener("click", onDblClick);
    } else {
      cardprogramm.addEventListener("click", handler)
    }

    function onDblClick(e) {
            let singleClickTimer = null
            singleClickTimer = setTimeout(function () {
                    clickCount = 0;
                }, 2000);
            clickCount++;
            if (clickCount === 2) {
                clearTimeout(singleClickTimer);
                clickCount = 0;
                handler()
            }
        }
    programmcardrow.appendChild(cardprogramm);
  });
}

const searchicon = document.getElementById("searchicon");
const search = document.getElementById("search");
const myModal = document.getElementById("myModal")


async function  search_program() {
  modal_content_h2.innerText = "";
  if (search.value.length) {
    const { programs } = await searchF({
      search_pattern: search.value,
    });
    if (!programs.length) {
      modal_content_h2.innerText = lenguage[`${leng}`].no_data;
      search.value = "";
      ulTag.style.display="none"
      pagination(0, 0, {});
    } else {
      pagination(1, 1, programs);
    }
  } else {
    const { pages_count } = await getPageCount();
    await pagination(pages_count, 1);
  }

  myModal.style.display = "none";
}

searchicon.addEventListener("click", search_program);

async function searchF(data) {
  const formData = new FormData();
  for (const key in data) {
    formData.append(key, data[key]);
  }
  try {
    const response = await fetch(
      `${server_url}search_programs/${leng}`,
      {
        method: "POST",
        body: formData,
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
