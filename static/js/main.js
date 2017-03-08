$(document).ready(function(){

  // Input form validation
  var $text = $('input[type="text"]');
  var $textarea = $('textarea');
  var $submit = $('input[type="submit"]');

  $submit.prop('disabled', true);
  $text.on('keyup', checkStatus);
  $textarea.on('keyup', checkStatus);


function checkStatus() {
    var status = ($.trim($text.val()) === '' || $.trim($textarea.val()) === '');
    $submit.prop('disabled', status);
}

})
