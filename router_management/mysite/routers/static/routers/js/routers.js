$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-router .modal-content").html("");
        $("#modal-router").modal("show");
      },
      success: function (data) {
        $("#modal-router .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#router-table tbody").html(data.html_router_list);
          $("#modal-router").modal("hide");
        }
        else {
          $("#modal-router .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create router
  $(".js-create-router").click(loadForm);
  $("#modal-router").on("submit", ".js-router-create-form", saveForm);

  // Update router
  $("#router-table").on("click", ".js-update-router", loadForm);
  $("#modal-router").on("submit", ".js-router-update-form", saveForm);

  // Delete router
  $("#router-table").on("click", ".js-delete-router", loadForm);
  $("#modal-router").on("submit", ".js-router-delete-form", saveForm);

});
