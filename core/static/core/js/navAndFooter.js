const data = {
  arm: {
    home: "Գլխավոր",
    about: "Մեր մասին",
    organization: "Կազմակերպություն",
    product: "Արտադրանք",
    report: "Հաշվետվություն",
    programs: "Ծրագրեր",
    announcements: "Հայտարարություններ",
    archive: "Արխիվ",
    contact: "Կապ",
    f_addres_title: "«Մարտունու կանանց համայնքային խորհուրդ» ՀԿ",
    f_addres_addres: "ՀՀ․ Գեղարքունիքի մարզ, ք․ Մարտունի 1402, Կամոյի 17,",
    f_addres_email: "kananc7@gmail.com",
    f_addres_phone: "+37494211396",
  },
  eng: {
    home: "Home",
    about: "About us",
    organization: "Organization",
    product: "Product",
    report: "Report",
    programs: "Programs",
    announcements: "Announcements",
    archive: "Archive",
    contact: "Contact",
    f_addres_title: "«Martunu Women's Community Council»NGO",
    f_addres_addres: "RA: Gegharkunik marz, c. Martuni 1402, Kamoi 17,",
    f_addres_email: "kananc7@gmail.com",
    f_addres_phone: "+37494211396",
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

  const home = this.document.getElementById("home");
  const home_m = this.document.getElementById("home_m");
  const about = this.document.getElementById("about");
  const about_m = this.document.getElementById("aboutus");
  const organization = this.document.getElementById("organization");
  const organization_m = this.document.getElementById("organization_m");
  const product = this.document.getElementById("product");
  const product_m = this.document.getElementById("product_m");
  const report = this.document.getElementById("report");
  const report_m = this.document.getElementById("report_m");
  const programs = this.document.getElementById("programs");
  const programs_m = this.document.getElementById("programs_m");
  const announcements = this.document.getElementById("announcements");
  const announcements_m = this.document.getElementById("announcements_m");
  const archive = this.document.getElementById("archive");
  const archive_m = this.document.getElementById("archive_m");
  const contact = this.document.getElementById("contact");
  const contact_m = this.document.getElementById("contact_m");
  home_m.innerText = data[`${leng}`].home;
  home.innerText = data[`${leng}`].home;
  about.innerText = data[`${leng}`].about;
  about_m.innerText = data[`${leng}`].about;
  about_m.innerHTML += '<i class="fa-solid fa-sort-down"></i>';
  organization.innerText = data[`${leng}`].organization;
  organization_m.innerText = data[`${leng}`].organization;
  product.innerText = data[`${leng}`].product;
  product_m.innerText = data[`${leng}`].product;
  report.innerText = data[`${leng}`].report;
  report_m.innerText = data[`${leng}`].report;
  programs.innerText = data[`${leng}`].programs;
  programs_m.innerText = data[`${leng}`].programs;
  announcements.innerText = data[`${leng}`].announcements;
  announcements_m.innerText = data[`${leng}`].announcements;
  archive.innerText = data[`${leng}`].archive;
  archive_m.innerText = data[`${leng}`].archive;
  contact.innerText = data[`${leng}`].contact;
  contact_m.innerText = data[`${leng}`].contact;

  const f_home = this.document.getElementById("f_home");
  const f_about = this.document.getElementById("f_about");
  const f_product = this.document.getElementById("f_product");
  const f_programs = this.document.getElementById("f_programs");
  const f_report = this.document.getElementById("f_report");
  const f_archive = this.document.getElementById("f_archive");
  const f_contact = this.document.getElementById("f_contact");
  const f_announcements = this.document.getElementById("f_announcements");

  f_home.innerText = data[`${leng}`].home;
  f_about.innerText = data[`${leng}`].about;
  f_product.innerText = data[`${leng}`].product;
  f_programs.innerText = data[`${leng}`].programs;
  f_report.innerText = data[`${leng}`].report;
  f_announcements.innerText = data[`${leng}`].announcements;
  f_archive.innerText = data[`${leng}`].archive;
  f_contact.innerText = data[`${leng}`].contact;

  const f_addres_title = this.document.getElementById("f_addres_title");
  const f_addres_addres = this.document.getElementById("f_addres_addres");
  const f_addres_email = this.document.getElementById("f_addres_email");
  const f_addres_phone = this.document.getElementById("f_addres_phone");

  f_addres_title.innerText = data[`${leng}`].f_addres_title;
  f_addres_addres.innerText = data[`${leng}`].f_addres_addres;
  f_addres_email.innerText = data[`${leng}`].f_addres_email;
  f_addres_phone.innerText = data[`${leng}`].f_addres_phone;
});

const lengArm = document.getElementById("lengArm");
const lengEng = document.getElementById("lengEng");
const leng_Arm = document.getElementById("leng_Arm");
const leng_Eng = document.getElementById("leng_Eng");

lengArm.addEventListener("click", () => {
  localStorage.setItem("leng", "arm");
  location.replace(location.href);
});
lengEng.addEventListener("click", () => {
  localStorage.setItem("leng", "eng");
  location.replace(location.href);
});
leng_Arm.addEventListener("click", () => {
  localStorage.setItem("leng", "arm");
  location.replace(location.href);
});
leng_Eng.addEventListener("click", () => {
  localStorage.setItem("leng", "eng");
  location.replace(location.href);
});
