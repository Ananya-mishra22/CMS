document.getElementById("personForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent the form from submitting normally

    var colorTimeInput = document.getElementById("colorTime");
    var colorTime = parseInt(colorTimeInput.value) * 1000; // Convert seconds to milliseconds

    // Set color change information in localStorage
    localStorage.setItem('colorTime', colorTime);
    localStorage.setItem('color', 'red');


});