document.addEventListener('DOMContentLoaded', function () {
  const currentUrl = window.location.href;
  const navLinks = document.querySelectorAll('.navbar-nav a.nav-link');

  navLinks.forEach(function (link) {
    if (link.href === currentUrl) {
      link.classList.add('active');
    }
  });
});
