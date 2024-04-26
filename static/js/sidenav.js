// Define the function that toggles the 'close' class on the sidebar
function toggleSidebar() {
  let sidebar = document.querySelector(".sidebar");
  sidebar.classList.toggle("close");
}

// Event listener for arrows to show or hide submenus
let arrow = document.querySelectorAll(".arrow");
for (var i = 0; i < arrow.length; i++) {
  arrow[i].addEventListener("click", (e) => {
    let arrowParent = e.target.parentElement.parentElement; // Selecting the main parent of the arrow
    arrowParent.classList.toggle("showMenu");
  });
}

// Event listener for the sidebar toggle button
let sidebarBtn = document.querySelector(".toggle-sidebar");
console.log(sidebarBtn);
sidebarBtn.addEventListener("click", toggleSidebar); // Call the function to toggle the sidebar
