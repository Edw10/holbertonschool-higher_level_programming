('DIV#red_header').css('cursor', 'pointer');
$('DIV#red_header').on('click', function (event) {
  $('header').css('color', '#FF0000');
  $('DIV#red_header').css('cursor', 'auto');
});
