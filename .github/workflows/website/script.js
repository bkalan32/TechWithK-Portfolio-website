const menuIcon = document.querySelector(".menu-icon")
const container = document.querySelector(".container")

menuIcon.addEventListener("click", () => {
    container.classList.toggle("change")
});

const counter = document.querySelector(".counter-number");

async function updateCounter() {
    try {
        let response = await fetch('https://ohw6dn7dvbubpyuhxfpgg3ztyq0upctb.lambda-url.us-east-1.on.aws/');
        let data = await response.json();
        counter.innerHTML = `Views: ${data.views}`;
    } catch (error) {
        console.error('Error fetching counter:', error);
    }
}

updateCounter();
