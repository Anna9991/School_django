let header = $('.header');
let btns = $('.btn-reset');
const goTopBtn = document.querySelector('.gotopbtn');
window.addEventListener('scroll', checkHeight)

function checkHeight(){
  if(window.scrollY > 200) {
    goTopBtn.style.display = "block";
    header.css
        ({
          'background': '#fff',
          'color': '#4b5f6d',
          'border-bottom' : '#4b5f6d solid 5px'
        });
        btns.css({'color': '#4b5f6d'});
  } else {
    goTopBtn.style.display = "none"
    header.css
      ({
        'background': 'none',
        'color': '#fff',
        'border-bottom' : 'none'
      });
      btns.css({'color': '#fff'});
  }
}