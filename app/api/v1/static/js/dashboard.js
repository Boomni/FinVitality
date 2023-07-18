


var sidebarOpen = false;
var sidebar = document.getElementById("sidebar");

function openSidebar() {
  if(!sidebarOpen) {
    sidebar.classList.add("sidebar-responsive");
    sidebarOpen = true;
  }
}

function closeSidebar() {
  if(sidebarOpen) {
    sidebar.classList.remove("sidebar-responsive");
    sidebarOpen = false;
  }
}

document.addEventListener("DOMContentLoaded", function () {
  const dropdown = document.getElementById("subscription-dropdown");
  dropdown.style.display = "none";
});

function toggleSubscriptionsDropdown(event) {
  event.preventDefault();
  const dropdown = document.getElementById("subscription-dropdown");
  dropdown.style.display = dropdown.style.display === "none" ? "block" : "none";
}

function showSavings(event) {
  event.preventDefault();
  const savingsSection = document.getElementById("savings-section");
  const loansSection = document.getElementById("loans-section");
  savingsSection.style.display = "block";
  loansSection.style.display = "none";
  const dropdown = document.getElementById("subscription-dropdown");
  dropdown.style.display = "none";
}

function showLoans(event) {
  event.preventDefault();
  const savingsSection = document.getElementById("savings-section");
  const loansSection = document.getElementById("loans-section");
  savingsSection.style.display = "none";
  loansSection.style.display = "block";
  const dropdown = document.getElementById("subscription-dropdown");
  dropdown.style.display = "none";
}
function hideFlashMessages() {
  const flashMessages = document.querySelectorAll('.flash-messages p');
  flashMessages.forEach(function(flashMessage) {
      flashMessage.style.display = 'none';
  });
}
setTimeout(hideFlashMessages, 2500);