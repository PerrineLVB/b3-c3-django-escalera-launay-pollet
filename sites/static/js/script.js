document.addEventListener('DOMContentLoaded', function() {
        var currentPage = window.location.pathname;
        var navLinks = document.querySelectorAll('.navbar-nav a');

        navLinks.forEach(function(link) {
            if (link.getAttribute('href') === currentPage) {
                link.classList.add('active');
            }
        });
    });

document.getElementById('darkModeToggle').addEventListener('click',()=>{
    if (document.documentElement.getAttribute('data-bs-theme') == 'dark') {
        document.documentElement.setAttribute('data-bs-theme','light')
    }
    else {
        document.documentElement.setAttribute('data-bs-theme','dark')
    }
})