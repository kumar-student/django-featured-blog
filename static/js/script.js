$(document).ready(function() {
    $('.nav-controller').click(function() {
        $('nav').toggleClass('focus');
    });
    /*$('nav, .nav-controller').on('mouseover', function(event) {
        $('nav').addClass('focus');
    }).on('mouseout', function(event) {
        $('nav').removeClass('focus');
    })*/
});