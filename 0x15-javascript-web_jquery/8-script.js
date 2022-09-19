$(document).ready(function () {
  const movie = 'https://swapi-api.hbtn.io/api/films/?format=json';
  $.getJSON(movie, function (data) {
    for (const mv of data.results) {
      $('UL#list_movies').append(`<li>${mv.title}</li>`);
    }
  });
});
