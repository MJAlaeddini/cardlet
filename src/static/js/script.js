//test propojení JS s projektem

const cardletHeading = document.getElementById('cardletheading');

cardletHeading.addEventListener('click', function onClick(event) {
    cardletHeading.style.backgroundColor = "salmon";
    cardletHeading.style.color = "white";
    cardletHeading.innerText = "Kliknuto";
});