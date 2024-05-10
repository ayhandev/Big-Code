function updateChat() {
    $.ajax({
        url: '127.0.0.1:8000/messenger/',  
        method: 'GET',
        success: function(data) {
            $('#messages').html(data);
        },
        error: function(xhr, status, error) {
            console.error('Error:', error);
        }
    });
}

setInterval(updateChat, 2000);