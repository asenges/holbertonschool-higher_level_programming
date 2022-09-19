$(document).ready(function () {
  const salut = 'https://stefanbohacek.com/hellosalut/?lang=fr';
  $.getJSON(salut, function (data) {
    $('#hello').text(data.hello);
  });
});
