from selenium.webdriver.support.ui import Select
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


if __name__ == '__main__':
    try:
        page_url = 'http://suninjuly.github.io/execute_script.html'

        browser = webdriver.Chrome()
        browser.get(page_url)

        x = int(browser.find_element_by_id('input_value').text)
        result = str(calc(x))

        input_field = browser.find_element_by_id('answer')
        browser.execute_script("return arguments[0].scrollIntoView(true);", input_field)
        input_field.send_keys(result)

        chk_box = browser.find_element_by_id('robotCheckbox')
        chk_box.click()

        rad_btn = browser.find_element_by_id('robotsRule')
        rad_btn.click()

        btn = browser.find_element_by_class_name('btn')
        browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
        btn.click()

    except Exception as e:
        print(e)
    finally:
        time.sleep(15)
        browser.quit()
