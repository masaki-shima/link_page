const dropdowns = document.querySelectorAll('.dropdown');

dropdowns. forEach(dropdown => {
    const select = dropdown.querySelector('.select');
    const caret = dropdown.querySelector('.caret');
    const menu = dropdown.querySelector('.menu');
    const options = dropdown.querySelectorAll('.menu li');
    const selected = dropdown.querySelector('.selected');

    select.addEventListener('click', () => {
        select.classList.toggle('select-clicked');
        //Add the rotate styles to the caret element
        caret.classList.toggle('caret-rotate');
        //Add the open styles to the menu element
        menu.classList.toggle('menu-open');
    });

    options.forEach(option => {
        option.addEventListener('click', () => {
            selected.innerText = option.innerText;
            selected.classList.add("text-fade-in");
        setTimeout (() => {
            selected.classList.remove("text-fade-in");
        }, 300);

        select.classList.remove('select-clicked');
        caret.classList.remove('caret-rotate');
        menu.classList.remove('menu-open');
        options.forEach(option => {
            option.classList.remove('active');
        });
        option.classList.add('active');
    });
});

window.addEventListener("click", e => {
    //Get the dropdown size and position
    const size = dropdown.getBoundingClientRect();
    /*If the click is outside of the dropdown,
    also close the dropdown*/
    if(
    e.clientX < size.left ||
    e.clientX > size.right ||
    e.clientY < size.top ||
    e.clientY > size.bottom
    ) {    
    //Remove the clicked select styles from the select element
    select.classList.remove('select-clicked');

    select.classList.remove('select-clicked');
    //Remove the rotate styles from the caret elen
    caret.classList.remove('caret-rotate');
    //Remove the open styles from the menu element
    menu.classList.remove('menu-open');
    }
});
});