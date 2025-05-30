const startScroller = () => {
  const SCROLL_CONTENT_WIDTH = 300;
  const CONTENT_GAP = 50;
  const CONTENT_PADDING = 32;
  // testimonial wrapper
  const testimonialWrapper = document.querySelector('.testimonials');
  // testimonials
  const testimonials = document.querySelectorAll('.profile');
  // timeout for scroll
  let scrollIntervalTimer;

  const startScroll = () => {
    scrollIntervalTimer = setInterval(() => {
      const maxScroll = testimonialWrapper.scrollWidth - testimonialWrapper.clientWidth;
      const distanceFromRight = maxScroll - testimonialWrapper.scrollLeft;
      if (distanceFromRight <= 0) {
        testimonialWrapper.scrollTo({ left: 0, behavior: 'smooth' });
        return;
      }
      const nextItemIndex = Math.floor(testimonialWrapper.scrollLeft / (SCROLL_CONTENT_WIDTH + CONTENT_GAP)) + 1;
      testimonialWrapper.scrollTo({
        left: [...testimonials][nextItemIndex].offsetLeft - testimonialWrapper.offsetLeft - CONTENT_PADDING,
        behavior: 'smooth',
      });
    }, 3000);
  };

  testimonialWrapper.addEventListener('scroll', () => {
    const scrollLeft = testimonialWrapper.scrollLeft;
    const scrollWidth = testimonialWrapper.scrollWidth;
    const maxScroll = scrollWidth - testimonialWrapper.clientWidth;

    testimonialWrapper.classList.toggle('left-shadow', scrollLeft > 0);
    testimonialWrapper.classList.toggle('right-shadow', scrollLeft < maxScroll);
  });

  testimonialWrapper.addEventListener('pointerenter', () => {
    clearInterval(scrollIntervalTimer);
  });

  testimonialWrapper.addEventListener('pointerleave', () => {
    startScroll();
  });

  window.addEventListener('load', () => {
    startScroll();
  });
};

const navigatorToggle = () => {
  const navbarToggle = document.querySelector('.toggle i');

  navbarToggle.addEventListener('click', () => {
    const navbar = document.querySelector('.navbar-list');
    navbar.classList.toggle('active');
  });
};

const startImageCarousel = () => {
  // set to 0 to start from second item at index 1
  // why? Because we always show the first item at index 0, incase javascript load is delayed
  let myIndex = 0;
  const carousel = () => {
    let carouselItems = [...document.querySelectorAll('.slide-item')];

    if (myIndex >= carouselItems.length - 1) {
      // set to -1 to restart from first item at index 0
      myIndex = -1;
    }
    myIndex++;

    const itemToShow = carouselItems.splice(myIndex, 1).pop();
    itemToShow.classList.toggle('hide');
    carouselItems.forEach((item) => {
      item.classList.add('hide');
    });
  };

  setInterval(carousel, 2000);
};

startScroller();
navigatorToggle();
startImageCarousel();
