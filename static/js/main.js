
$(document).ready(function(){
    $('.menu').on('click', function(){
        $('ul').toggleClass('active');
    })
})

$(".alert-dismissible").fadeTo(2000, 500).slideUp(500, function(){
    $(".alert-dismissible").alert('close');
});

$('.slider').slick({
  speed: 300,
  slidesToShow: 4,
  slidesToScroll: 1,
  autoplay: true,
  autoplaySpeed: 2000,
  responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 3,
        infinite: true,
        dots: true
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }
    // You can unslick at a given breakpoint now by adding:
    // settings: "unslick"
    // instead of a settings object
  ]
});

window.sr = ScrollReveal({ duration: 1000 });
sr.reveal('.hero-text-container');
sr.reveal('.rectangle-image');
sr.reveal('.about-first');
sr.reveal('.about-second');
sr.reveal('.about-third');
sr.reveal('.services-inner');
sr.reveal('.profile');
sr.reveal('.contact-us');
