var a = 0;
$(window).scroll(function () {
    var oTop = $("#counter-box").offset().top - window.innerHeight;
    if (a == 0 && $(window).scrollTop() > oTop) {
        $(".counter").each(function () {
            var $this = $(this),
                countTo = $this.attr("data-number");
            $({
                countNum: $this.text()
            }).animate(
                {
                    countNum: countTo
                },

                {
                    duration: 3000,
                    easing: "swing",
                    step: function () {
                        $this.text(
                            Math.ceil(this.countNum).toLocaleString("en")
                        );
                    },
                    complete: function () {
                        $this.text(
                            Math.ceil(this.countNum).toLocaleString("en")
                        );
                    }
                }
            );
        });
        a = 1;
    }
});

const swiper = new Swiper('.mySwiper', {
    grabCursor: true,
    spaceBetween: 30,
    breakpoints:{
      767:{
        slidesPerView: 2
      }
    }
  });

