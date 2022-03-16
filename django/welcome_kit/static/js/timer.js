function timer() {
    const month = document.querySelector('.month');
    const day = document.querySelector('.day');
    const dayNumber = document.querySelector('.dayNumber');
    const time = document.querySelector('.time');
    const date = new Date();
    // init();

    month.removeChild(month.firstChild);
    day.removeChild(day.firstChild);
    dayNumber.removeChild(dayNumber.firstChild);
    time.removeChild(time.firstChild);

    const newMonth = convertMonthToEnglish(date.getMonth());
    const newDate = date.getDate();
    const newDay = convertDayToEnglish(date.getDay());
    const AM = checkAm(date.getHours());
    const newHours =
        date.getHours() % 12 >= 10
            ? `${date.getHours()} % 12)`
            : `0${date.getHours() % 12}`;
    const newMinutes =
        date.getMinutes() >= 10
            ? `${date.getMinutes()}`
            : `0${date.getMinutes()}`;

    month.appendChild(document.createTextNode(newMonth));
    dayNumber.appendChild(document.createTextNode(newDate));
    day.appendChild(document.createTextNode(newDay));
    time.appendChild(document.createTextNode(`${newHours}:${newMinutes}` + AM));
}

function convertDayToEnglish(day) {
    const dayArr = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
    return dayArr[day];
}

function convertMonthToEnglish(month) {
    const monthArr = [
        'Jan',
        'Feb',
        'Mar',
        'Apr',
        'May',
        'Jun',
        'Jul',
        'Aug',
        'Sep',
        'Nov',
        'Dec',
    ];
    return monthArr[month];
}
function checkAm(hour) {
    if (hour >= 12) {
        return 'PM';
    } else {
        return 'AM';
    }
}

timer();
setInterval(timer, 3600);
