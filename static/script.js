let flippedCards = [];
let successCount = 0;

function revealImage(cell) {
    const card = cell.querySelector('.card');
    const image = card.getAttribute('data-image');

    if (flippedCards.length < 2 && !flippedCards.includes(cell)) {
        flippedCards.push(cell);
        card.innerHTML = `<img src="${image}" alt="Revealed Image">`;

        if (flippedCards.length === 2) {
            setTimeout(checkMatch, 1000);
        }
    }
}

function checkMatch() {
    const [cell1, cell2] = flippedCards;
    const image1 = cell1.querySelector('.card').getAttribute('data-image');
    const image2 = cell2.querySelector('.card').getAttribute('data-image');

    if (image1 === image2) {
        successCount += 2;
        if (successCount === 16) {
            document.getElementById('successMessage').style.display = 'block';
        }
    } else {
        cell1.querySelector('.card').innerHTML = '<img src="static/img/blank.jpg" alt="Hidden Image">';
        cell2.querySelector('.card').innerHTML = '<img src="static/img/blank.jpg" alt="Hidden Image">';
    }

    flippedCards = [];
}
