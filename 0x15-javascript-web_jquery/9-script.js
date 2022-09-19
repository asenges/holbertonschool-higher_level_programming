$(document).ready(function () {
  const msg = 'https://fourtonfish.com/hellosalut/?lang=fr';
  $.getJSON(msg, function (data) {
    $('#hello').text(data.hello);
  });
});
