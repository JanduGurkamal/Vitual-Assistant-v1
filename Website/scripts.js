document.addEventListener('DOMContentLoaded', () => {
    createStarfield();
    window.addEventListener('scroll', () => {
        const header = document.querySelector('header');
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });
});

function learnMore() {
    window.location.href = "#features";
}

function createStarfield() {
    const starfield = document.createElement('div');
    starfield.classList.add('starfield');
    document.body.appendChild(starfield);

    for (let i = 0; i < 100; i++) {
        const star = document.createElement('div');
        star.classList.add('star');
        star.style.top = `${Math.random() * 100}vh`;
        star.style.left = `${Math.random() * 100}vw`;
        starfield.appendChild(star);
    }
}
