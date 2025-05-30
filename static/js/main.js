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

  testimonialWrapper.addEventListener('mouseenter', () => {
    clearInterval(scrollIntervalTimer);
  });

  testimonialWrapper.addEventListener('mouseleave', () => {
    startScroll();
  });

  window.addEventListener('load', () => {
    startScroll();
  });
};

startScroller();
