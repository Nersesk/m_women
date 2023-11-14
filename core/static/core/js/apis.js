const server_url = main_url()
window.addEventListener("load", async function (event) {
  const leng = this.localStorage.getItem("leng");
  const { announcements } = await getAllData(leng);
  const index_container = document.getElementById("index_container");
  for (let item of announcements) {
    let length = 0;
    const cardblock = document.createElement("div");
    cardblock.classList.add("cardblock");
    const card = document.createElement("div");
    card.classList.add("card");
    const img_container = document.createElement("div");
    img_container.classList.add("img-container");
    const img = document.createElement("img");
    img.setAttribute("src", `${item.image}`);
    const card_details = document.createElement("div");
    card_details.classList.add("card-details");
    const h3 = document.createElement("h3");
    h3.innerHTML = item.name;
    const cardblocktext = document.createElement("div");
    cardblocktext.classList.add("cardblocktext");
    cardblocktext.innerHTML = `<p>${item.name}</p>`;
    card_details.appendChild(h3);
    let desc = item.description.replace(/<\/p>/g, "");
    desc = desc.replace(/<p>/g, "");
    desc = desc.substring(0, 398);
    desc += "...";
    card_details.innerHTML += `<p>${desc}</p>`;
    img_container.appendChild(img);
    card.appendChild(img_container);
    card.appendChild(card_details);
    card.addEventListener("click", () => {
      localStorage.setItem("announcecolId", item.url);

      if(item.type === 'job'){
        window.location.href  = `${server_url}job_announcement/${item.id}`
      }else{
        window.location.href =`${server_url}open_competition/${item.id}`
      }
    });
    cardblock.appendChild(card);
    cardblock.appendChild(cardblocktext);
    index_container.appendChild(cardblock);
  }
});

async function getAllData(leng) {
  try {
    const response = await fetch(
      `${server_url}get_latest_announcements/${leng}`,
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
