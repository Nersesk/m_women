const data_index = {
  arm: {
    title_1: "Մարտունու կանանց համայնքային խորհուրդ",
    descriptio:
      "Մեր կազմակերպությունը Գեղարքունիքի մարզի առաջատար հասարակական կազմակերպություններից է։ Հիմնադրվելով 2000 թ–ին՝ այն գործունեություն է իրականացնում առողջապահության, բնապահպանության, սոցիալական և համայնքային զարգացման ոլորտներում՝ կարևորելով բնակչության անմիջական ներգրավվածությունը տարբեր խնդիրների լուծման գործընթացում: Մեր խորհրդի ջանքերով Գեղարքունիքի մարզում վերակառուցվել են բուժկետեր, կառուցվել նախակրթարաններ, հիմնվել է սոցիալական ձեռնարկություն, որտեղ աշխատում են բացառապես հաշմանդամություն ունեցող անձիք: Փորձում ենք նպաստել համայնքում ապահով և պաշտպանված քաղաքացու ձևավորմանը։",
    title_2: "Մեր առավելությունները",
    read_more_button: "Կարդալ ավելին",
    title_3: "Հայտարարություններ",
    advantages_1_p: "ԱՆՀԱՏԱԿԱՆ",
    advantages_1_span: "ՄՈՏԵՑՈՒՄ",
    advantages_2_p: "ՍԵՂՄ",
    advantages_2_span: "ԺԱՄԿԵՏՆԵՐ",
    advantages_3_p: "ՊՐՈՖԵՍԻՈՆԱԼ",
    advantages_3_span: "ԹԻՄ",
    advantages_4_p: "ՄՇՏԱԿԱՆ",
    advantages_4_span: "ԱՃ",
    advantages_5_p: "ԱՐԱԳ",
    advantages_5_span: "ԱՐՁԱԳԱՆՔ",
    advantages_6_p: "ՄԱՏՉԵԼԻ",
    advantages_6_span: "ԳԻՆ",
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
    title_1: "Martuni Women's Community Council",
    descriptio:
      "Our organization is one of the leading non-governmental organizations of Gegharkunik region. Founded in 2000, it carries out activities in the fields of healthcare, environmental protection, social and community development, emphasizing the direct involvement of the population in the process of solving various problems. With the efforts of our council, medical centers were rebuilt in Gegharkunik region, preschools were built, and a social enterprise was established, where only people with disabilities work. We try to contribute to the formation of a safe and protected citizen in the community.",
    title_2: "Our advantages",
    read_more_button: "Read more",
    title_3: "Announcements",
    advantages_1_p: "INDIVIDUAL",
    advantages_1_span: "APPROACH",
    advantages_2_p: "PRESS",
    advantages_2_span: "DEADLINES",
    advantages_3_p: "PROFESSIONAL",
    advantages_3_span: "TEAM",
    advantages_4_p: "PERMANENTLY",
    advantages_4_span: "GROWTH  ",
    advantages_5_p: "FAST",
    advantages_5_span: "ECHO",
    advantages_6_p: "AFFORDABLE",
    advantages_6_span: "PRICE",
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

  const title_1 = this.document.getElementById("title_1");
  const descriptio = this.document.getElementById("descriptio");
  const more = this.document.getElementById("more");
  const title_2 = this.document.getElementById("title_2");
  const title_3 = this.document.getElementById("title_3");
  const advantages_1_p = this.document.getElementById("advantages_1_p");
  const advantages_2_p = this.document.getElementById("advantages_2_p");
  const advantages_3_p = this.document.getElementById("advantages_3_p");
  const advantages_4_p = this.document.getElementById("advantages_4_p");
  const advantages_5_p = this.document.getElementById("advantages_5_p");
  const advantages_6_p = this.document.getElementById("advantages_6_p");

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

  home.innerText = data_index[`${leng}`].home;
  home_m.innerText = data_index[`${leng}`].home;
  about.innerText = data_index[`${leng}`].about;
  about_m.innerText = data_index[`${leng}`].about;
  about_m.innerHTML += '<i class="fa-solid fa-sort-down"></i>';
  organization.innerText = data_index[`${leng}`].organization;
  organization_m.innerText = data_index[`${leng}`].organization;
  product.innerText = data_index[`${leng}`].product;
  product_m.innerText = data_index[`${leng}`].product;
  report.innerText = data_index[`${leng}`].report;
  report_m.innerText = data_index[`${leng}`].report;
  programs.innerText = data_index[`${leng}`].programs;
  programs_m.innerText = data_index[`${leng}`].programs;
  announcements.innerText = data_index[`${leng}`].announcements;
  announcements_m.innerText = data_index[`${leng}`].announcements;
  archive.innerText = data_index[`${leng}`].archive;
  archive_m.innerText = data_index[`${leng}`].archive;
  contact.innerText = data_index[`${leng}`].contact;
  contact_m.innerText = data_index[`${leng}`].contact;

  const f_home = this.document.getElementById("f_home");
  const f_about = this.document.getElementById("f_about");
  const f_product = this.document.getElementById("f_product");
  const f_programs = this.document.getElementById("f_programs");
  const f_report = this.document.getElementById("f_report");
  const f_archive = this.document.getElementById("f_archive");
  const f_contact = this.document.getElementById("f_contact");
  const f_announcements = this.document.getElementById("f_announcements");

  f_home.innerText = data_index[`${leng}`].home;
  f_about.innerText = data_index[`${leng}`].about;
  f_product.innerText = data_index[`${leng}`].product;
  f_programs.innerText = data_index[`${leng}`].programs;
  f_report.innerText = data_index[`${leng}`].report;
  f_announcements.innerText = data_index[`${leng}`].announcements;
  f_archive.innerText = data_index[`${leng}`].archive;
  f_contact.innerText = data_index[`${leng}`].contact;

  const f_addres_title = this.document.getElementById("f_addres_title");
  const f_addres_addres = this.document.getElementById("f_addres_addres");
  const f_addres_email = this.document.getElementById("f_addres_email");
  const f_addres_phone = this.document.getElementById("f_addres_phone");

  f_addres_title.innerText = data_index[`${leng}`].f_addres_title;
  f_addres_addres.innerText = data_index[`${leng}`].f_addres_addres;
  f_addres_email.innerText = data_index[`${leng}`].f_addres_email;
  f_addres_phone.innerText = data_index[`${leng}`].f_addres_phone;

  title_1.innerText = data_index[`${leng}`].title_1;
  descriptio.innerText = data_index[`${leng}`].descriptio;
  more.innerText = data_index[`${leng}`].read_more_button;
  title_2.innerText = data_index[`${leng}`].title_2;
  advantages_1_p.innerText = data_index[`${leng}`].advantages_1_p;
  advantages_1_p.innerHTML += `<span id="advantages_1_span" class="smallp2">${
    data_index[`${leng}`].advantages_1_span
  }</span>`;
  advantages_2_p.innerText = data_index[`${leng}`].advantages_2_p;
  advantages_2_p.innerHTML += `<span id="advantages_2_span" class="smallp2">${
    data_index[`${leng}`].advantages_2_span
  }</span>`;
  advantages_3_p.innerText = data_index[`${leng}`].advantages_3_p;
  advantages_3_p.innerHTML += `<span id="advantages_3_span" class="smallp2">${
    data_index[`${leng}`].advantages_3_span
  }</span>`;
  advantages_4_p.innerText = data_index[`${leng}`].advantages_4_p;
  advantages_4_p.innerHTML += `<span id="advantages_4_span" class="smallp2">${
    data_index[`${leng}`].advantages_4_span
  }</span>`;
  advantages_5_p.innerText = data_index[`${leng}`].advantages_5_p;
  advantages_5_p.innerHTML += `<span id="advantages_5_span" class="smallp2">${
    data_index[`${leng}`].advantages_5_span
  }</span>`;
  advantages_6_p.innerText = data_index[`${leng}`].advantages_6_p;
  advantages_6_p.innerHTML += `<span id="advantages_6_span" class="smallp2">${
    data_index[`${leng}`].advantages_6_span
  }</span>`;
  title_3.innerText = data_index[`${leng}`].title_3;
});
