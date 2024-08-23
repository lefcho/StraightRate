let originalComment = '';
const commentArea = document.querySelector('.review-form textarea');
const rating = document.getElementById('rating-value');

// Store the original values of the textarea and rating
if (commentArea) {
    originalComment = commentArea.value;
}
let originalRating = rating ? rating.value : 0;

// Get star elements
const stars = document.querySelectorAll('.star');

// Function to make stars interactive or not
function setStarsInteractive(interactive) {
    stars.forEach(star => {
        if (interactive) {
            star.classList.remove('disabled');
            star.addEventListener('click', handleStarClick);
            star.addEventListener('mouseover', handleStarHover);
            star.addEventListener('mouseout', handleStarMouseOut);
        } else {
            star.classList.add('disabled');
            star.removeEventListener('click', handleStarClick);
            star.removeEventListener('mouseover', handleStarHover);
            star.removeEventListener('mouseout', handleStarMouseOut);
        }
    });
}

// Handle star hover
function handleStarHover() {
    resetStars();
    highlightStars(this.getAttribute('data-value'));
}

// Handle star mouse out
function handleStarMouseOut() {
    resetStars();
    highlightStars(rating.value);
}

// Handle star click
function handleStarClick() {
    rating.value = this.getAttribute('data-value');
    highlightStars(rating.value);
}

// Function to reset all stars to default (unfilled)
function resetStars() {
    stars.forEach(star => star.classList.remove('filled'));
}

// Function to highlight stars up to the specified value
function highlightStars(rating) {
    for (let i = 0; i < rating; i++) {
        stars[i].classList.add('filled');
    }
}

// When the "Edit" button is clicked
document.getElementById('edit-review-btn').addEventListener('click', function() {
    // Enable the textarea
    if (commentArea) {
        commentArea.disabled = false;
    }

    // Show the Save and Cancel buttons
    document.getElementById('save-review-btn').classList.remove('hidden');
    document.getElementById('cancel-review-btn').classList.remove('hidden');

    // Hide the Edit button
    this.classList.add('hidden');

    // Make stars interactive
    setStarsInteractive(true);
});

// When the "Cancel" button is clicked
document.getElementById('cancel-review-btn').addEventListener('click', function() {
    // Reset the textarea to its original value
    if (commentArea) {
        commentArea.value = originalComment;
        commentArea.disabled = true;
    }

    // Reset the stars to their original state
    stars.forEach((star, index) => {
        star.classList.remove('filled');
        if (index < originalRating) {
            star.classList.add('filled');
        }
    });

    // Hide the Save and Cancel buttons
    document.getElementById('save-review-btn').classList.add('hidden');
    document.getElementById('cancel-review-btn').classList.add('hidden');

    // Show the Edit button
    document.getElementById('edit-review-btn').classList.remove('hidden');

    // Make stars non-interactive
    setStarsInteractive(false);
});

// Initialize stars as non-interactive
setStarsInteractive(false);
