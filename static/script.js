document.addEventListener("DOMContentLoaded", function() {
var inputFields = document.querySelectorAll('input[name="url"]');
var inventoryQuantities = document.querySelectorAll('.inventory-quantity');

hy
複製
inputFields.forEach(function(input, index) {
input.addEventListener("input", function() {
inventoryQuantities[index].textContent = "";
});
});
});