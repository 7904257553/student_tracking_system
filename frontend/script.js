document.getElementById('trainCameraButton').addEventListener('click', function() {
    const name = document.getElementById('name').value;
    if (name.trim() === '') {
        alert('Please enter a name');
        return;
    }

    fetch('/train_camera', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name: name })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').textContent = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').textContent = 'An error occurred.';
    });
});

document.getElementById('trainFolderButton').addEventListener('click', function() {
    fetch('/train_folder', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').textContent = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').textContent = 'An error occurred.';
    });
});