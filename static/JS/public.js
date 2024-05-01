
document.getElementById('publish-button').addEventListener('click', function() {
    document.getElementById('publish-modal').style.display = 'block';
});

// Закрыть модальное окно при нажатии на кнопку "Close"
document.getElementsByClassName('close')[0].addEventListener('click', function() {
    document.getElementById('publish-modal').style.display = 'none';
});

// Отправить форму через AJAX
document.getElementById('confirm-publish').addEventListener('click', function() {
    var form = document.getElementById('publish-form');
    var formData = new FormData(form);
    fetch(form.action, {
        method: form.method,
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Code published successfully!');
            document.getElementById('publish-modal').style.display = 'none'; // Закрыть модальное окно после успешной публикации
        } else {
            alert('Failed to publish code.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});


