$('DIV#red_header').css('cursor', 'pointer');
$('DIV#red_header').on('click', function (event) {
  $('header').addClass('red');
  $('DIV#red_header').css('cursor', 'auto');
});
