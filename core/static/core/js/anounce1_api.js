const leng = this.localStorage.getItem("leng");
const server_url = main_url()
const cur_url_list = request_url().split('/')
const elem_type = cur_url_list[cur_url_list.length-2];
const elem_id = cur_url_list[cur_url_list.length-1];
const lenguage = {
  arm: {
    v_name: "Աշխատանքի անվանումը՝",
    organization:
      "Կազմակերպությունը՝ «Մարտունու կանանց համայնքային խորհուրդ» ՀԿ",
    duration: "Աշխատանքի տևողությունը՝",
    assessment_service: "Գնահատման ծառայության նկարագիրը․",
    application_submission: "Հայտերի ներկայացման կարգը.",
    about_the_organization: "Կազմակերպության մասին.",
    contacts: "Կոնտակտներ",
    requirements_appraiser: "Պահանջներ գնահատողին.",
    file_modal_open_text:
      "<p class='file_modal_open_text_p'><span>Անհրաժեշտ փաստաթղթերի ցանկ </span><span>(կարող եք ներբեռնել՝ սեղմելով համապատասխան բառերի վրա)</span></p>",
  },
  eng: {
    v_name: "Job Title:",
    organization: "Organization: «Martunu Women's Community Council»",
    duration: "Duration of work:",
    assessment_service: "Assessment Service Description:",
    application_submission: "Application submission procedure.",
    about_the_organization: "About the organization.",
    contacts: "Contacts",
    requirements_appraiser: "Requirements to the appraiser.",
    file_modal_open_text:
      "<p class='file_modal_open_text_p'><span>List of necessary documents</span><span>(you can download by clicking on the relevant words</span>)</p>",
  },
};
window.addEventListener("load", async function () {
  let url = '';
  if(elem_type === 'job_announcement'){
        url = `${server_url}get_announcment_detail/${leng}/${elem_id}`;
      }
   else{
        url = `${server_url}get_open_competition_detail/${leng}/${elem_id}`;
      }
  const announc = await getAnnounc(url);
  const anounceinfosmalltext_img = this.document.getElementById(
    "anounceinfosmalltext_img"
  );
  anounceinfosmalltext_img.setAttribute(
    "src",
    `${announc.image}`
  );
  const anouncesmalltxt_h2 =
    this.document.getElementById("anouncesmalltxt_h2");
  const anouncesmalltxt_p = this.document.getElementById("anouncesmalltxt_p");
  anouncesmalltxt_h2.innerText = announc.name ? announc.name : announc.title;
  anouncesmalltxt_p.innerHTML = announc.name
    ? `${lenguage[`${leng}`].v_name} ${announc.name} <br />${
        lenguage[`${leng}`].organization
      } <br />  ${lenguage[`${leng}`].duration} ${announc.duration}: ${
        announc.description
      }`
    : `${announc.description} ${announc.article}`;
  if (announc.name) {
    const anouncep_p = this.document.getElementById("anouncep_p");
    anouncep_p.innerHTML = `${lenguage[`${leng}`].assessment_service}`;
    const anounceinfodotes_ul = this.document.getElementById(
      "anounceinfodotes_ul"
    );
    anounceinfodotes_ul.innerHTML += announc.assessment_desc;
    const anouncep_p2 = this.document.getElementById("anouncep_p2");
    anouncep_p2.innerText = `${lenguage[`${leng}`].application_submission}`;
    const application_procedure = this.document.getElementById(
      "application_procedure"
    );

    application_procedure.innerHTML += announc.application_procedure;
    const anouncep_p3 = this.document.getElementById("anouncep_p3");
    anouncep_p3.innerText = `${lenguage[`${leng}`].about_the_organization}`;
    const about_the_organization = this.document.getElementById(
      "about_the_organization"
    );
    about_the_organization.innerHTML += announc.about_company;
    const anouncep_4 = this.document.getElementById("anouncep_4");
    anouncep_4.innerText = `${lenguage[`${leng}`].requirements_appraiser}`;
    const anounceinfodotes_ul2 = this.document.getElementById(
      "anounceinfodotes_ul2"
    );
    anounceinfodotes_ul2.innerHTML += announc.appraiser_requirements;
    const contacts = this.document.getElementById("contacts");
    contacts.innerText = `${lenguage[`${leng}`].contacts}`;
  } else {
    const block = this.document.querySelectorAll(".block");
    block.forEach((item) => {
      item.remove();
    });
    const anounceinfotext_contacts = document.getElementById(
      "anounceinfotext_contacts"
    );
    anounceinfotext_contacts.innerHTML += `${
      lenguage[`${leng}`].file_modal_open_text
    }`;

    anounceinfotext_contacts.addEventListener("click", () => {
      const modal = document.createElement("div");
      const modal_ash_content = document.createElement("div");
      const cloase = document.createElement("div");
      const cloaseIcon = document.createElement("i");
      const modal_main = document.createElement("div");
      modal.classList.add("modal_ash");
      modal_ash_content.classList.add("modal_ash_content");
      cloaseIcon.classList.add("fa-solid");
      cloaseIcon.classList.add("fa-xmark");
      cloase.classList.add("cloase_modal");
      cloase.appendChild(cloaseIcon);

      cloase.addEventListener("click", () => {
        modal.remove();
      });
      announc.required_files.forEach((item) => {
        const modal_main_file = document.createElement("div");
        const file = document.createElement("div");
        file.classList.add("file");
        file.innerText = item.name;
        file.addEventListener("click", () => {
          let url = `${item.url}`;
          const a = document.createElement("a");
          a.href = url;
          a.download = url;
          document.body.appendChild(a);
          a.click();
          document.body.removeChild(a);
        });
        modal_main_file.classList.add("modal_main_file");
        modal_main_file.appendChild(file);
        modal_main.appendChild(modal_main_file);
      });
      modal_ash_content.appendChild(cloase);
      modal_ash_content.appendChild(modal_main);
      modal.appendChild(modal_ash_content);

      document.body.appendChild(modal);
    });
  }
});

async function getAnnounc(url) {
  try {

    const response = await fetch(url, {
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
