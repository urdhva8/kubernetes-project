// ================= NAVBAR =================
const navbar = document.getElementById('navbar');

if (navbar) {
    window.addEventListener('scroll', () => {
        navbar.classList.toggle('scrolled', window.scrollY > 50);
    });

    navbar.classList.add('scrolled');
}

// ================= MOBILE NAV =================
const navToggle = document.getElementById('navToggle');
const navLinks = document.getElementById('navLinks');

if (navToggle && navLinks) {
    navToggle.addEventListener('click', () => {
        navLinks.classList.toggle('open');
    });
}

// ================= SCROLL REVEAL =================
const revealElements = document.querySelectorAll(
    '.place-card, .why-card, .team-card, .value-card, .testimonial-card'
);

if (revealElements.length > 0) {

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
}

// ================= NEWSLETTER =================
const newsletterForm = document.querySelector('.newsletter-form');

if (newsletterForm) {

    newsletterForm.addEventListener('submit', (e) => {

        e.preventDefault();

        const btn = newsletterForm.querySelector('button');

        if (!btn) return;

        btn.textContent = '✓ Subscribed!';
        btn.style.background = '#2d7a2d';
        btn.style.color = '#fff';

        setTimeout(() => {

            btn.textContent = 'Subscribe';
            btn.style.background = '';
            btn.style.color = '';

            const input = newsletterForm.querySelector('input');

            if (input) {
                input.value = '';
            }

        }, 3000);
    });

    const button = newsletterForm.querySelector('button');

    if (button) {

        button.addEventListener('click', (e) => {

            const input = newsletterForm.querySelector('input');

            if (!input || !input.value || !input.value.includes('@')) {

                if (input) {
                    input.style.outline = '3px solid #e53e3e';

                    setTimeout(() => {
                        input.style.outline = '';
                    }, 2000);
                }

                e.preventDefault();
            }
        });
    }
}

// ================= SMOOTH SCROLL =================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {

    anchor.addEventListener('click', function (e) {

        const href = this.getAttribute('href');

        if (href === '#') return;

        const target = document.querySelector(href);

        if (target) {

            e.preventDefault();

            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// ================= PAGE FADE =================
document.body.style.opacity = '0';
document.body.style.transition = 'opacity 0.5s ease';

window.addEventListener('load', () => {
    document.body.style.opacity = '1';
});
