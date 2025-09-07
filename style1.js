function sendMessage() {
    var userInput = document.getElementById("user-input").value.trim();
    if (userInput === "") return;  // Prevent sending empty messages

    var chatBox = document.getElementById("chat-box");
    var userHtml = "<p><strong>You:</strong> " + escapeHtml(userInput) + "</p>";
    chatBox.innerHTML += userHtml;

    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/get?msg=" + encodeURIComponent(userInput), true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var botResponse = "<p><strong>Bot:</strong> " + escapeHtml(xhr.responseText) + "</p>";
            chatBox.innerHTML += botResponse;
            chatBox.scrollTop = chatBox.scrollHeight;  // Auto scroll to bottom
        }
    };
    xhr.send();
    document.getElementById("user-input").value = "";  // Clear the input field
}

function escapeHtml(text) {
    var map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
    };
    return text.replace(/[&<>"']/g, function(m) { return map[m]; });
}
