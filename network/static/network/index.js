// when clicking heart shape turn to red
$(document).ready(function () {
  $(".like-button").click(function () {
    $(this).find("i").toggleClass("fas far text-danger");
  });
})
