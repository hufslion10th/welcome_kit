const btn = document.getElementById('start-btn');

function slideInput() {
    if (this.firstChild.nodeType == 3) {
        this.firstElementChild.className = 'visible';
        this.removeChild(this.firstChild);
    }
}
btn.addEventListener('click', slideInput);
