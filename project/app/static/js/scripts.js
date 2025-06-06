var swiper = new Swiper(".team-slider", {
    loop: true,
    grabCursor: true,
    spaceBetween: 20,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    autoplay: {
      delay: 2500, // 2.5 seconds delay between slides
      disableOnInteraction: false, // Allow autoplay to continue even after user interaction
    },
    breakpoints: {
      0: {
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 2,
      },
      991: {
        slidesPerView: 3,
      },
    },
  });
