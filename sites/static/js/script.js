document.addEventListener('DOMContentLoaded', function() {
        var currentPage = window.location.pathname;
        var navLinks = document.querySelectorAll('.navbar-nav a');

        navLinks.forEach(function(link) {
            if (link.getAttribute('href') === currentPage) {
                link.classList.add('active');
            }
        });
    });
