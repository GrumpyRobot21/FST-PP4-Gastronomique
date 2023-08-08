// Manual carousel controls
let currentIndex = 0;

// show the current image
function updateCarousel() {
  const carousel = document.querySelector('.carousel');
  const images = carousel.querySelectorAll('img');
  carousel.style.transform = `translateX(-${currentIndex * (images[0].offsetWidth + 10)}px)`;
}

// Move to previous image
function prevImage() {
  const carousel = document.querySelector('.carousel');
  const images = carousel.querySelectorAll('img');
  currentIndex = (currentIndex - 1 + images.length) % images.length;
  updateCarousel();
}

// Move to next image
function nextImage() {
  const carousel = document.querySelector('.carousel');
  const images = carousel.querySelectorAll('img');
  currentIndex = (currentIndex + 1) % images.length;
  updateCarousel();
}