document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("form-contato");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = new FormData(form);

    const response = await fetch("/enviar_mensagem", {
      method: "POST",
      body: formData,
    });

    const result = await response.json();

    alert(result.mensagem);
    form.reset();
  });
});

console.log("JS externo funcionando!");

// Exemplo do slider
const track = document.querySelector('.slider-track');
const buttons = document.querySelectorAll('.slider-btn');
let currentIndex = 0;
const totalSlides = track.children.length;

function goToSlide(index) {
  track.style.transform = `translateX(-${index * 100}%)`;
  currentIndex = index;
  buttons.forEach((btn, i) => {
    btn.classList.toggle('bg-blue-600', i === index);
    btn.classList.toggle('bg-blue-400', i !== index);
  });
}

buttons.forEach(btn => {
  btn.addEventListener('click', () => goToSlide(parseInt(btn.dataset.slide)));
});

// Auto slide
setInterval(() => {
  let nextIndex = (currentIndex + 1) % totalSlides;
  goToSlide(nextIndex);
}, 4000);

