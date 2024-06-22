import bot from "./assets/bot.svg";
import user from "./assets/user.svg";

const form = document.querySelector("form");
const chatContainer = document.querySelector("#chat_container");

let loadInterval;

function loader(element) {
  element.textContent = "";

  loadInterval = setInterval(() => {
    element.textContent += ".";
    if (element.textContent === "....") {
      element.textContent = "";
    }
  }, 300);
}

function typeText(element, text) {
  const paletteBox = document.createElement("div")
  paletteBox.classList.add("palette")
  console.log(JSON.parse(text))
  JSON.parse(text).forEach(color => {
    const palette = document.createElement("div")
    palette.style.width = "2rem"
    palette.style.height = "2rem"
    palette.style.backgroundColor = color

    paletteBox.appendChild(palette)
  });

  element.appendChild(paletteBox)
}

// generate unique ID for each message div of bot
// necessary for typing text effect for that specific reply
// without unique ID, typing text will work on every element
function generateUniqueId() {
  const timestamp = Date.now();
  const randomNumber = Math.random();
  const hexadecimalString = randomNumber.toString(16);

  return `id-${timestamp}-${hexadecimalString}`;
}

function chatStripe(isAi, value, uniqueId) {
  return `
  <div class="wrapper ${isAi && "ai"}">
  <div class="chat">
      <div class="profile">
          <img 
            src=${isAi ? bot : user} 
            alt="${isAi ? "bot" : "user"}" 
          />
      </div>
      <div class="message" id=${uniqueId}>${value}</div>
  </div>
</div>
    `;
}

async function handleSubmite(e) {
  e.preventDefault();
  const data = new FormData(form);

  //  user's chatstripe
  chatContainer.innerHTML += chatStripe(false, data.get("prompt"));

  form.reset();

  // bot's chatStripe
  const uniqueId = generateUniqueId();
  chatContainer.innerHTML += chatStripe(true, "", uniqueId);

  chatContainer.scrollTop = chatContainer.scrollHeight;

  const messageDiv = document.getElementById(uniqueId);
  loader(messageDiv);

  // fetch data from server
  const response = await fetch("http://127.0.0.1:5000/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ description: data.get("prompt") }),
  });
  clearInterval(loadInterval);
  messageDiv.innerHTML = "";

  if (response.ok) {
    const data = await response.json();

    typeText(messageDiv, JSON.stringify(data));
  } else {
    const err = await response.text();

    messageDiv.innerHTML = "Something Went Wrong";
    alert(err)
  }
}

form.addEventListener("submit", handleSubmite);

// handling submit by pressing enter
form.addEventListener("keyup", (e) => {
  if (e.keyCode === "13") {
    handleSubmite(e);
  }
});