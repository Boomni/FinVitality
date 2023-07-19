  var sidebarOpen = false;
  var sidebar = document.getElementById("sidebar");

  function openSidebar() {
    if (!sidebarOpen) {
      sidebar.classList.add("sidebar-responsive");
      sidebarOpen = true;
    }
  }

  function closeSidebar() {
    if (sidebarOpen) {
      sidebar.classList.remove("sidebar-responsive");
      sidebarOpen = false;
    }
  }
  function hideFlashMessages() {
    const flashMessages = document.querySelectorAll('.flash-messages p');
    flashMessages.forEach(function (flashMessage) {
      flashMessage.style.display = 'none';
    });
  }
  setTimeout(hideFlashMessages, 2500);