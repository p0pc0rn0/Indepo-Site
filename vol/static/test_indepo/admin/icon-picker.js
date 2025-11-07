document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("[data-icon-picker]").forEach(function (picker) {
    function updateSelection() {
      picker.querySelectorAll(".icon-picker__option").forEach(function (option) {
        var input = option.querySelector('input[type="radio"]');
        option.classList.toggle("is-selected", input && input.checked);
      });
    }

    picker.addEventListener("change", function (event) {
      if (event.target.matches('input[type="radio"]')) {
        updateSelection();
      }
    });

    updateSelection();
  });
});
