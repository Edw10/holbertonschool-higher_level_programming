$('DIV#add_item').css('cursor', 'pointer');
$('DIV#add_item').on('click', function (event) {
  $('UL.my_list').append('<li>Item</li>');
});
