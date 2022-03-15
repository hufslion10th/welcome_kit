const btn = document.getElementById('start-btn');
const input = document.querySelector('.hide');

function slideInput() {
    if (this.firstChild.nodeType == 3) {
        this.firstElementChild.firstElementChild.className = 'visible';
        this.removeChild(this.firstChild);
    }
}

function submitName(e) {
    if (e.keyCode == 13) {
        login.submit();
    }
}
btn.addEventListener('click', slideInput);
input.addEventListener('keydown', submitName);
