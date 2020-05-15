$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (swm) {
  for (const i in swm.results) {
    $('UL#list_movies').append('<li>' + swm.results[i].title + '</li>');
  }
});
