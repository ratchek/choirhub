// Define the function that toggles the 'close' class on the sidebar
function toggleSidebar() {
  let sidebar = document.querySelector(".sidebar");
  sidebar.classList.toggle("close");
}

// Event listener for arrows to show or hide submenus
let nav_dropdowns = document.querySelectorAll(".nav_li_with_dropdown");
nav_dropdowns.forEach((dropdown) => {
  dropdown.addEventListener("click", (e) => {
    dropdown.classList.toggle("showMenu");
  });
});

// Event listener for the sidebar toggle button
let sidebarBtn = document.querySelector(".toggle-sidebar");
console.log(sidebarBtn);
sidebarBtn.addEventListener("click", toggleSidebar); // Call the function to toggle the sidebar
