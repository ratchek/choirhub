document.addEventListener('DOMContentLoaded', function() {
  // Select all loop buttons by class name
  const loopButtons = document.querySelectorAll('.loopButton');

  loopButtons.forEach(button => {
    button.addEventListener('click', function() {
      // Find the nearest audio element within the same container
      const audio = button.parentElement.querySelector('audio');
      if (audio) {
        // Toggle the loop property
        audio.loop = !audio.loop;

        // Switch css to show it's active
        button.classList.toggle('active', audio.loop);
      }
    });
  });
});
