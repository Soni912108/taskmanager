console.log('JavaScript code is executing');


// get all checkboxes and their labels
const checkboxes = document.querySelectorAll('input[name=completed]');
const labels = document.querySelectorAll('label[for^=completed]');

// hide the checkboxes
checkboxes.forEach((checkbox) => {
    checkbox.style.display = 'none';
});

// add an extra label for each checkbox to serve as a toggle button
labels.forEach((label) => {
    const checkboxId = label.getAttribute('for');
    const checkbox = document.getElementById(checkboxId);
    const newLabel = document.createElement('label');
    newLabel.textContent = label.textContent;
    newLabel.addEventListener('click', function() {
        checkbox.checked = !checkbox.checked;
        if (checkbox.checked) {
            newLabel.textContent = 'Completed';
        } else {
            newLabel.textContent = 'Incomplete';
        }
        
        // make an AJAX request to update the task status
        const xhr = new XMLHttpRequest();
        xhr.open('POST', `/dashboard/update-task-status/${checkbox.dataset.taskId}/`, true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.onload = function() {
            if (this.status === 200) {
                console.log('Task status updated successfully');
            } else {
                console.log('Error updating task status');
            }
        };
        xhr.send(`completed=${checkbox.checked}`);
    });
    label.insertAdjacentElement('afterend', newLabel);
});

