function toggleTopBar() {
    let topbar = document.getElementById('top-nav-mobile');
    topbar.classList.toggle("top-nav-open");
    topbar.classList.toggle("top-nav-closed");
}


// Event listener for the sidebar toggle button
let menuButton = document.querySelector(".top-nav-toggle");
console.log(menuButton);
menuButton.addEventListener("click", toggleTopBar); // Call the function to toggle the sidebar
