$('DIV#toggle_header').css('cursor', 'pointer');
$('DIV#toggle_header').on('click', function (event) {
  $('header').toggleClass(function () {
    if ($('header').hasClass('red')) {
      $('header').removeClass('red');
      return 'green';
    } else {
      $('header').removeClass('green');
      return 'red';
    }
  });
});
