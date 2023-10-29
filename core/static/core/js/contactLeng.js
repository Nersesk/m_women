const dataa = {
  arm: {
    title_1: "Կապ մեզ հետ",
    p_1: "Ընդհանուր հարցերի համար`",
    p_2: "Ընդհանուր հարցերի համար`",
    p_3: "Սոցիալական բաժին",
    p_4: "Հաղորդակցություն և հրապարակումներ`",
    p_5: "Թեժ գիծ`",
    p_6: "Գնումների բաժին`",
    p_7: "Ֆինանսական բաժին`",
    p_8: "Այլ հարթակներ`",
    p_9: "էլ․ Փոստ`",
    p_10: "Ընդհանուրհարցերի համար`",
    p_11: "Կրթական բաժին`",
    p_12: "Հասցե`",
    p_13: "Կամոյի 17, ք․ Մարտունի, Գեղարքունիքի մարզ, ՀՀ, 1402",
    p_14: "Մարտունու կանանց համայնքային",
    p_15: "խորհուրդ",
    p_16: "Կրթապնակ",
    p_17: "Մարտունի Ինֆոտուն",
    p_18: "Կանանց աջակցման կենտրոն Գեղարքունիքի մարզում",
    email: "Էլ․հասցե",
    tel: "Հեռախոս",
    send: "Ուղարկել",
    textarea: "Ողջույն!...",
  },
  eng: {
    title_1: "Contact us",
    p_1: "For general questions",
    p_2: "Educational department",
    p_3: "Social department",
    p_4: "Communications and Publications",
    p_5: "Hot line",
    p_6: "Purchasing Department",
    p_7: "Financial department",
    p_8: "Other platforms",
    p_9: "email",
    p_10: "For general questions",
    p_11: "Educational department",
    p_12: "addres",
    p_13: "Kamoi 17, c. Martuni, Gegharkunik region, RA, 1402",
    p_14: "Martuni women's community",
    p_15: "MWCC NGO",
    p_16: "EduPalette",
    p_17: "Martuni Infotun",
    p_18: "Women's support center in Gegharkunik region",
    email: "Email",
    tel: "Phone Number",
    send: "Send",
    textarea: "Hello!...",
  },
};

window.addEventListener("load", async function (event) {
  let leng = localStorage.getItem("leng");
  if (!leng) {
    localStorage.setItem("leng", "arm");
    leng = "arm";
  }

  const title_1 = this.document.getElementById("title_1");
  title_1.innerText = dataa[`${leng}`].title_1;

  const email = this.document.getElementById("email");
  email.setAttribute("placeholder", dataa[`${leng}`].email);

  const tel = this.document.getElementById("tel");
  tel.setAttribute("placeholder", dataa[`${leng}`].tel);

  const send = this.document.getElementById("send");
  send.setAttribute("value", dataa[`${leng}`].send);

  const textarea = this.document.getElementById("textarea");
  textarea.setAttribute("placeholder", dataa[`${leng}`].textarea);

  const p_1 = this.document.getElementById("p_1");
  p_1.innerText = dataa[`${leng}`].p_1;
  const p_2 = this.document.getElementById("p_2");
  p_2.innerText = dataa[`${leng}`].p_2;
  const p_3 = this.document.getElementById("p_3");
  p_3.innerText = dataa[`${leng}`].p_3;
  const p_4 = this.document.getElementById("p_4");
  p_4.innerText = dataa[`${leng}`].p_4;
  const p_5 = this.document.getElementById("p_5");
  p_5.innerText = dataa[`${leng}`].p_5;
  const p_6 = this.document.getElementById("p_6");
  p_6.innerText = dataa[`${leng}`].p_6;
  const p_7 = this.document.getElementById("p_7");
  p_7.innerText = dataa[`${leng}`].p_7;
  const p_8 = this.document.getElementById("p_8");
  p_8.innerText = dataa[`${leng}`].p_8;
  const p_9 = this.document.getElementById("p_9");
  p_9.innerText = dataa[`${leng}`].p_9;
  const p_10 = this.document.getElementById("p_10");
  p_10.innerText = dataa[`${leng}`].p_10;
  const p_11 = this.document.getElementById("p_11");
  p_11.innerText = dataa[`${leng}`].p_11;
  const p_12 = this.document.getElementById("p_12");
  p_12.innerText = dataa[`${leng}`].p_12;
  const p_13 = this.document.getElementById("p_13");
  p_13.innerText = dataa[`${leng}`].p_13;
  const p_14 = this.document.getElementById("p_14");
  p_14.innerText = dataa[`${leng}`].p_14;
  const p_15 = this.document.getElementById("p_15");
  p_15.innerText = dataa[`${leng}`].p_15;
  const p_16 = this.document.getElementById("p_16");
  p_16.innerText = dataa[`${leng}`].p_16;
  const p_17 = this.document.getElementById("p_17");
  p_17.innerText = dataa[`${leng}`].p_17;
  const p_18 = this.document.getElementById("p_18");
  p_18.innerText = dataa[`${leng}`].p_18;
});

async function getAllData(data) {
  try {
    const response = await fetch(
      ` https://xn--29ae4dgic.xn--y9a3aq/send_email`,
      {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
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

const send = document.getElementById("send");
const email = document.getElementById("email");
const tel = document.getElementById("tel");
const textarea = document.getElementById("textarea");
send.addEventListener("click", async (e) => {
  e.preventDefault();
  if (email.value && tel.value && textarea.value) {
    const data = {
      from_email: email.value,
      phone_number: tel.value,
      message_text: textarea.value,
    };
    await getAllData(data);
  }
});
