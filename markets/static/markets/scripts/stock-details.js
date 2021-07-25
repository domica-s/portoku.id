var interval = 1000 * 60 * 5;
var webSlug = "{{ name }}";
$(document).ready(function () {
  setInterval(function () {
    $.ajax({
      type: "POST",
      url: "{% url 'getUpdatedStockPrice' %}",
      data: {
        'slug': webSlug,
        'csrfmiddlewaretoken': "{{ csrf_token }}",
      },
      success: function (response) {
        $("#price").empty();
        $("#price").append(response["price"]);
      },
      error: function (response) {
        alert("An error occured: " + response);
      },
    });
  }, interval);
});
