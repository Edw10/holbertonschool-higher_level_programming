$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (hofr) {
  $('DIV#hello').append(hofr.hello);
});
