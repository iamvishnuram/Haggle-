let canFlip = true;
    
function flipCard(card) {
    if (!canFlip) {
        return;
    }

    // canFlip = false;

    const cardInner = card.querySelector('.card-inner');
    const icon = cardInner.querySelector('.card-front i');

    // Zoom effect
    cardInner.style.transform = 'scale(1.2)';
    setTimeout(() => {
        cardInner.style.transform = '';
    }, 300);

    // Change the icon to unlock
    icon.classList.remove('fa-lock');
    icon.classList.add('fa-unlock');

    setTimeout(() => {
        card.classList.toggle('flipped');
        const value = parseInt(cardInner.querySelector('.card-back h2').innerText);

        if (value > 50) {
            startFallingPapers();
            stopFallingAfterTimeout();
        }

        setTimeout(() => {
            canFlip = true;
            if (card.classList.contains('flipped')) {
                card.parentNode.removeChild(card);
                adjustCardPositions();
            }
        }, 3000);
    }, 800);
}

let isFalling = false;

function startFallingPapers() {
    if (!isFalling) {
        isFalling = true;
        fall();
    }
}

function fall() {
    const container = document.getElementById('container');
    const paper = document.createElement('div');
    paper.className = 'paper';
    paper.style.left = Math.random() * window.innerWidth + 'px';
    paper.style.top = Math.random() * window.innerHeight + 'px';
    paper.style.background = getRandomColor();
    container.appendChild(paper);

    setTimeout(() => {
        paper.remove();
    }, 2000);

    if (isFalling) {
        requestAnimationFrame(fall);
    }
}

function stopFallingAfterTimeout() {
    setTimeout(() => {
        isFalling = false;
    }, 2000);
}

function getRandomColor() {
    const colors = ['#3498db', '#2ecc71', '#e74c3c', '#f39c12', '#9b59b6', '#1abc9c', '#f1c40f', '#34495e', '#ecf0f1', 'yellow'];
    return colors[Math.floor(Math.random() * colors.length)];
}

