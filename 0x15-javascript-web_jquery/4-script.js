// Toggles between classes

$('DIV#toggle_header').on('click', function () {
  if ($(this).hasClass('red')) {
    $(this).removeClass('red').addClass('green');
  } else {
    $(this).removeClass('green').addClass('red');
  }
});
