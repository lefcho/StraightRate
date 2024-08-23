
// Store the original values in a variable
let originalValues = {};

// When the "Edit" button is clicked
document.getElementById('edit-review-btn').addEventListener('click', function() {
    // Enable all input fields
    document.querySelectorAll('.review-form textarea').forEach(input => {
        input.disabled = false;

        // Store the original value of each input field
        originalValues[input.name] = input.value;
    });

    // Show the Save and Cancel buttons
    document.getElementById('save-review-btn').classList.remove('hidden');
    document.getElementById('cancel-review-btn').classList.remove('hidden');

    // Hide the Edit button
    this.classList.add('hidden');
});

// When the "Cancel" button is clicked
document.getElementById('cancel-review-btn').addEventListener('click', function() {
    // Reset all input fields to their original values
    document.querySelectorAll('.review-form textarea').forEach(input => {
        input.value = originalValues[input.name];
        input.disabled = true;  // Disable the input fields again
    });

    // Hide the Save and Cancel buttons
    document.getElementById('save-review-btn').classList.add('hidden');
    document.getElementById('cancel-review-btn').classList.add('hidden');

    // Show the Edit button
    document.getElementById('edit-review-btn').classList.remove('hidden');
});
