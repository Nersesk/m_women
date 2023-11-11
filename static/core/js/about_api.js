const leng = this.localStorage.getItem("leng");
const server_url = main_url()
const lenguage = {
  arm: {
    btn: "ավելին",
    or_btn: "ավելի քիչ",
    cooperation: "տարի համագործակցություն<br />",
    program: "իրականացված ծրագիր",
  },
  eng: {
    btn: "Show more",
    or_btn: "show less",
    cooperation: "years of cooperation<br />",
    program: "implemented program",
  },
};
window.addEventListener("load", async function () {
  const partner = await getAllPartners(1);
  const { staff_members, next_page } = await getAllStaff(1);
  appendPartners(partner);
  appendStaff(staff_members, next_page);
});

async function getAllPartners(page) {
  try {
    const response = await fetch(
      `${server_url}get_partners/${leng}/${page}`,
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

async function getAllStaff(page) {
  try {
    const response = await fetch(
      `${server_url}get_staff/${leng}/${page}`,
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

async function appendStaff(staff_members, next_page) {
  const members = this.document.getElementById("members");
  staff_members.forEach((staff) => {
    const member = document.createElement("div");
    member.classList.add("member");
    const member_img = document.createElement("div");
    member_img.classList.add("member_img");
    const img = document.createElement("img");
    img.setAttribute("src", `${staff.image}`);
    img.setAttribute("alt", "member");
    const h2 = document.createElement("h2");
    h2.innerText = staff.name;
    const p = document.createElement("p");
    p.innerText = staff.position;
    member_img.appendChild(img);
    member.appendChild(member_img);
    member.appendChild(h2);
    member.appendChild(p);
    members.appendChild(member);
  });
  if (next_page !== null) {
    genMoreButton(next_page);
  }
}

async function appendNextStaff(page) {
  const { staff_members, next_page } = await getAllStaff(page);
  appendStaff(staff_members, next_page);
}
async function appendNextStaffPartners(page) {
  const partner = await getAllPartners(page);
  appendPartners(partner);
}

function appendPartners(partners) {
  const { business_partners, next_page } = partners;
  const partnerrow = this.document.getElementById("partnerrow");
  business_partners.forEach((partner) => {
    const item = document.createElement("div");
    item.classList.add("item");
    item.classList.add("animated");
    item.classList.add("wow");
    item.classList.add("fadeIn");
    const img = document.createElement("img");
    console.log(partner.image)
    img.setAttribute("src", `${partner.image}`);
    img.setAttribute("alt", "partner");
    const overlay = document.createElement("div");
    overlay.classList.add("overlay");
    overlay.classList.add("right-overlay");
    const textoverlay = document.createElement("div");
    textoverlay.classList.add("textoverlay");
    textoverlay.innerHTML = `${partner.duration}
    ${lenguage[`${leng}`].cooperation}
    ${partner.projects_count}
    ${lenguage[`${leng}`].program}
    `;
    overlay.appendChild(textoverlay);
    item.appendChild(img);
    item.appendChild(overlay);
    partnerrow.appendChild(item);
  });
  if (next_page !== null) {
    genPartnersMoreButton(next_page);
  }
}

function genMoreButton(next_page) {
  const show_more_1 = this.document.getElementById("show_more_1");
  const button = document.createElement("button");
  button.classList.add("button_global");
  button.innerText = lenguage[`${leng}`].btn;
  button.addEventListener("click", async (event) => {
    button.remove();
    await appendNextStaff(next_page);
  });
  show_more_1.appendChild(button);
}

function genPartnersMoreButton(next_page) {
  const show_more_1 = this.document.getElementById("show_more_2");
  const button = document.createElement("button");
  button.classList.add("button_global");
  button.innerText = lenguage[`${leng}`].btn;
  button.addEventListener("click", async (event) => {
    button.remove();
    await appendNextStaffPartners(next_page);
  });
  show_more_1.appendChild(button);
}
