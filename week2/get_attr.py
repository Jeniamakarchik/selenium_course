from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


if __name__ == '__main__':
    page_url = 'http://suninjuly.github.io/get_attribute.html'

    browser = webdriver.Chrome()
    browser.get(page_url)

    treasure = browser.find_element_by_id('treasure')
    x = int(treasure.get_attribute('valuex'))
    result = calc(x)

    input_field = browser.find_element_by_id('answer')
    input_field.send_keys(str(result))

    chk_box = browser.find_element_by_id('robotCheckbox')
    chk_box.click()

    rad_btn = browser.find_element_by_id('robotsRule')
    rad_btn.click()

    btn = browser.find_element_by_class_name('btn')
    btn.click()

    time.sleep(15)
    browser.quit()



