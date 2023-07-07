function hideFlashMessages() {
    const flashMessages = document.querySelectorAll('.flash-messages p');
    flashMessages.forEach(function(flashMessage) {
        flashMessage.style.display = 'none';
    });
}
    
setTimeout(hideFlashMessages, 2500);