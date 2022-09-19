$(document).ready(function () {
  const names = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  $.getJSON(names, function (data) {
    $('#character').text(data.name);
  });
});
