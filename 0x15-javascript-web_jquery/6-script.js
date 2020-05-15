$('DIV#update_header').css('cursor', 'pointer');
$('DIV#update_header').on('click', function (event) {
  $('header').text('New Header!!!');
  $('DIV#update_header').css('cursor', 'auto');
});
