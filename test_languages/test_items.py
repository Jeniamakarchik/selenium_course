from selenium.common.exceptions import NoSuchElementException


def test_contains_cart_button(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

    browser.get(url)
    try:
        button = browser.find_element_by_class_name('btn-add-to-basket')
        assert True
    except NoSuchElementException:
        assert False, "Button doesn't exist on the page."
