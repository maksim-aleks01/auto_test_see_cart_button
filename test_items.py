import time #Для проверки
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_cart_button(browser):
    browser.get(link)
    time.sleep(30) #Для визуальной оценки результатов теста в барузере

    actual_result = browser.find_elements_by_css_selector("#add_to_basket_form > button") 
    assert str(actual_result) != "[]", "Cart button is missing"
