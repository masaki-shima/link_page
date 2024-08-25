document.addEventListener('DOMContentLoaded', () => {
    const selects = document.querySelectorAll('.select');
    const menus = document.querySelectorAll('.menu');

    selects.forEach(select => {
        select.addEventListener('click', (event) => {
            const clickedMenu = select.nextElementSibling;
            
            // 他の全てのメニューを閉じる
            menus.forEach(menu => {
                if (menu !== clickedMenu) {
                    menu.classList.remove('menu-open');
                    menu.style.height = '0';
                    menu.style.marginBottom = '0';
                    const otherSelect = menu.previousElementSibling;
                    otherSelect.classList.remove('select-clicked');
                    otherSelect.querySelector('.caret').classList.remove('caret-rotate');
                }
            });

            // 現在のメニューの開閉をトグル
            if (clickedMenu.classList.contains('menu-open')) {
                clickedMenu.classList.remove('menu-open');
                select.classList.remove('select-clicked');
                clickedMenu.style.height = '0';
                clickedMenu.style.marginBottom = '0';
                select.querySelector('.caret').classList.remove('caret-rotate');
            } else {
                const menuHeight = clickedMenu.scrollHeight + 'px';
                clickedMenu.classList.add('menu-open');
                select.classList.add('select-clicked');
                clickedMenu.style.height = menuHeight;
                clickedMenu.style.marginBottom = '10px'; // メニューの高さに応じて下のコンテンツを下げる
                select.querySelector('.caret').classList.add('caret-rotate');

                // メニューが画面外に出ないようにスクロールする
                const menuRect = clickedMenu.getBoundingClientRect();
                const isOverflowing = menuRect.bottom > window.innerHeight;

                if (isOverflowing) {
                    window.scrollBy({
                        top: menuRect.bottom - window.innerHeight,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });

    // ドキュメント全体のクリックイベントを追加し、メニュー外をクリックした場合にメニューを閉じる
    document.addEventListener('click', (event) => {
        if (!event.target.closest('.dropdown')) {
            menus.forEach(menu => {
                menu.classList.remove('menu-open');
                menu.style.height = '0';
                menu.style.marginBottom = '0';
                const select = menu.previousElementSibling;
                select.classList.remove('select-clicked');
                select.querySelector('.caret').classList.remove('caret-rotate');
            });
        }
    });
});
