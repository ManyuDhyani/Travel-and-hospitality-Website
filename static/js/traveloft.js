var listEl = document.querySelector('.home-grid.products-grid.products-grid--max-4');
var btnLeftEl = document.querySelector('#left-btn');
var btnRightEl = document.querySelector('#right-btn');
count = 0;
btnLeftEl.addEventListener("click", function(e) {
    count++;
    listEl.style.left = count * 300 + 'px';
    if (count > -2) {
        btnRightEl.style.display = 'block';
    }
    if (count >= 0) {
        btnLeftEl.style.display = 'none';
    }
});
btnRightEl.addEventListener("click", function(e) {
    count--;
    listEl.style.left = count * 300 + 'px';
    if (count < 0) {
        btnLeftEl.style.display = 'block';
    }
    if (count <= -2) {
        btnRightEl.style.display = 'none';
    }
});


$(document).ready(function(){
    $(".dropdown, .btn-group").hover(function(){
        var dropdownMenu = $(this).children(".dropdown-menu");
        if(dropdownMenu.is(":visible")){
            dropdownMenu.parent().toggleClass("open");
        }
    });
});

