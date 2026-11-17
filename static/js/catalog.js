function getDaysWord(number) {
    const lastTwo = Math.abs(number) % 100;
    const lastOne = lastTwo % 10;

    if (lastTwo >= 11 && lastTwo <= 19) {
        return 'дней';
    }
    if (lastOne === 1) {
        return 'день';
    }
    if (lastOne >= 2 && lastOne <= 4) {
        return 'дня';
    }
    return 'дней';
}

document.querySelectorAll('.tour-days').forEach(el => {
    const days = parseInt(el.dataset.days, 10);
    if (!isNaN(days)) {
        el.textContent = `/ ${days} ${getDaysWord(days)}`;
    }
});
