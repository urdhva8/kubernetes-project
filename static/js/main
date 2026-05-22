// Navbar scroll effect
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 50);
});
navbar.classList.add('scrolled'); // Always show background

// Mobile nav toggle
const navToggle = document.getElementById('navToggle');
const navLinks = document.getElementById('navLinks');
if (navToggle && navLinks) {
    navToggle.addEventListener('click', () => {
        navLinks.classList.toggle('open');
    });
}

// Scroll reveal animation
const revealElements = document.querySelectorAll('.place-card, .why-card, .team-card, .value-card, .testimonial-card');
const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
        if (entry.isIntersecting) {
            setTimeout(() => {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }, index * 80);
            revealObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.1 });

revealElements.forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    revealObserver.observe(el);
});

// Newsletter form
const newsletterForm = document.querySelector('.newsletter-form');
if (newsletterForm) {
    newsletterForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const btn = newsletterForm.querySelector('button');
        btn.textContent = '✓ Subscribed!';
        btn.style.background = '#2d7a2d';
        btn.style.color = '#fff';
        setTimeout(() => {
            btn.textContent = 'Subscribe';
            btn.style.background = '';
            btn.style.color = '';
            newsletterForm.querySelector('input').value = '';
        }, 3000);
    });

    newsletterForm.querySelector('button').addEventListener('click', (e) => {
        const input = newsletterForm.querySelector('input');
        if (!input.value || !input.value.includes('@')) {
            input.style.outline = '3px solid #e53e3e';
            setTimeout(() => input.style.outline = '', 2000);
            e.preventDefault();
        }
    });
}

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href === '#') return;
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
});

// Page load fade-in
document.body.style.opacity = '0';
document.body.style.transition = 'opacity 0.5s ease';
window.addEventListener('load', () => {
    document.body.style.opacity = '1';
});
