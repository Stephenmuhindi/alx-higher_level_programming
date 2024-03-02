$(document).ready(function () {
  $("#add_item").click(function () {
    var newListItem = $("<li>Item</li>");
    $("ul.my_list").append(newListItem);
  });
});
