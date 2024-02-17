document.addEventListener('DOMContentLoaded', function() {
    var currentPage = window.location.pathname;
    var navLinks = document.querySelectorAll('.navbar-nav a');

    navLinks.forEach(function(link) {
        if (link.getAttribute('href') === currentPage) {
            link.classList.add('active');
        }
    });

    // Dark mode
    document.getElementById('darkModeToggle').addEventListener('click', function () {
        if (document.documentElement.getAttribute('data-bs-theme') === 'dark') {
            document.documentElement.setAttribute('data-bs-theme', 'light');
        } else {
            document.documentElement.setAttribute('data-bs-theme', 'dark');
        }
        localStorage.setItem('darkMode', document.documentElement.getAttribute('data-bs-theme') === 'dark');
    });
    if (localStorage.getItem('darkMode') === 'true') {
        document.documentElement.setAttribute('data-bs-theme', 'dark');
    }
});
