// get all the edit buttons in the dashboard
const editButtons = document.querySelectorAll('.edit-button');

// loop through each edit button
editButtons.forEach((button) => {
  // add a click event listener to each button
  button.addEventListener('click', (event) => {
    // get the task element
    const taskElement = button.closest('.task');

    // get the task title and description elements
    const titleElement = taskElement.querySelector('.title');
    const descriptionElement = taskElement.querySelector('.description');

    // make the title and description elements editable
    titleElement.setAttribute('contenteditable', true);
    descriptionElement.setAttribute('contenteditable', true);
    titleElement.classList.add('editable');
    descriptionElement.classList.add('editable');

    // hide the edit button
    button.style.display = 'none';

    // show the save button
    const saveButton = taskElement.querySelector('.save-button');
    saveButton.style.display = 'inline-block';
  });
});

// get all the save buttons in the dashboard
const saveButtons = document.querySelectorAll('.save-button');

// loop through each save button
saveButtons.forEach((button) => {
  // add a click event listener to each button
  button.addEventListener('click', (event) => {
    // get the task element
    const taskElement = button.closest('.task');

    // get the task title and description elements
    const titleElement = taskElement.querySelector('.title');
    const descriptionElement = taskElement.querySelector('.description');

    // make the title and description elements non-editable
    titleElement.setAttribute('contenteditable', false);
    descriptionElement.setAttribute('contenteditable', false);
    titleElement.classList.remove('editable');
    descriptionElement.classList.remove('editable');

    // hide the save button
    button.style.display = 'none';

    // show the edit button
    const editButton = taskElement.querySelector('.edit-button');
    editButton.style.display = 'inline-block';

    // send an ajax request to update the task data
    const formData = new FormData();
    formData.append('title', titleElement.textContent);
    formData.append('description', descriptionElement.textContent);
    formData.append('csrfmiddlewaretoken', '{{ csrf_token }}');

    fetch(`/tasks/${taskElement.dataset.taskId}/update/`, {
      method: 'POST',
      body: formData
    })
      .then(response => {
        // check the response status
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
      })
      .catch(error => console.error('Error:', error));
  });

  // hide the save button initially
  button.style.display = 'none';
});
