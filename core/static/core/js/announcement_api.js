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
const leng = this.localStorage.getItem("leng");
const announcements_id = document.getElementById("announcements_id");

window.addEventListener("load", async function () {
  const { pages_count } = await getPageCount();
  pagination(pages_count, 1);
});

async function getPageCount() {
  try {
    const response = await fetch(
      `https://տեստէջ.հայ/get_announcements_page_count`,
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

async function pagination(totalPages, page, data) {
  let programs_data;
  if (!data) {
    const { announcements } = await getAnnouncements(page);
    programs_data = announcements;
  } else {
    programs_data = data;
  }

  await throwAnnouncements(programs_data);
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

  async function throwAnnouncements(announcements) {
    announcements_id.innerHTML = "";
    for (let item of announcements) {
      const h3 = document.createElement("h3");
      h3.innerText = item.name;
      const p = document.createElement("p");
      let desc = item.description.replace(/<\/p>/g, "");
      desc = desc.replace(/<p>/g, "");
      desc = desc.substring(0, 398);
      desc += "...";
      p.innerHTML = desc;
      const a = document.createElement("a");
      const button = document.createElement("button");
      button.innerText = lenguage[`${leng}`].btn;
      a.appendChild(button);
      a.setAttribute("href", "anounce1.html");
      a.addEventListener("click", (e) => {
        e.preventDefault();
        localStorage.setItem("announcecolId", item.url);
        window.location.href = "anounce1.html";
      });
      const announcecol = document.createElement("div");
      announcecol.classList.add("announcecol");
      announcecol.classList.add("anouncetext");
      announcecol.appendChild(h3);
      announcecol.appendChild(p);
      announcecol.appendChild(a);
      const announcecol_2 = document.createElement("div");
      announcecol_2.classList.add("announcecol");
      const img = document.createElement("img");
      img.setAttribute("src", `https://xn--29ae4dgic.xn--y9a3aq${item.image}`);
      img.setAttribute("alt", "announcecol");
      announcecol_2.appendChild(img);
      const announcerow = document.createElement("div");
      announcerow.classList.add("announcerow");
      announcerow.appendChild(announcecol_2);
      announcerow.appendChild(announcecol);
      const anounce = document.createElement("div");
      anounce.classList.add("anounce");
      anounce.appendChild(announcerow);
      announcements_id.appendChild(anounce);
    }
  }
}

async function getAnnouncements(page) {
  try {
    const response = await fetch(
      `https://տեստէջ.հայ/get_announcment_list/${leng}/${page}`,
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

const searchicon = document.getElementById("searchicon");
const search = document.getElementById("search");
const myModal = document.getElementById("myModal");

searchicon.addEventListener("click", async () => {
  modal_content_h2.innerText = "";
  if (search.value.length) {
    console.log("001");
    const { announcements } = await searchF({
      search_pattern: search.value,
    });

    if (!announcements.length) {
      pagination(1, 1, []);
      modal_content_h2.innerText = lenguage[`${leng}`].no_data;
      search.value = "";
    } else {
      pagination(1, 1, announcements);
    }
  } else {
    const { pages_count } = await getPageCount();
    pagination(pages_count, 1);
  }

  myModal.style.display = "none";
});

async function searchF(data) {
  const formData = new FormData();
  for (const key in data) {
    formData.append(key, data[key]);
  }

  try {
    const response = await fetch(
      `https://xn--29ae4dgic.xn--y9a3aq/search_announcments/${leng}`,
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
