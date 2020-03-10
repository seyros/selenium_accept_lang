import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

messages = {
    'ru': 'Добавить в корзину',
    'en': 'Add to basket',
    'fr': 'Ajouter au panier',
    'es': 'Añadir al carrito'
}


def test_user_lang_on_add_button(get_browser):
    browser = get_browser[0]
    lang = get_browser[1]
    browser.get(link)
    time.sleep(30)
    addbutton = browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert addbutton, 'Не найдена кнопка добавления товара в корзину'
    addmessage = addbutton.text
    if lang in messages.keys():
        assert addmessage == messages[lang], \
            f'Для языка браузера \'{lang}\' ожидалось сообщение: \'{messages[lang]}\', а получено: \'{addmessage}\''
