from selenium.webdriver.support.ui import Select
from selenium import webdriver
import math
import os
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


if __name__ == '__main__':
    try:
        page_url = 'http://suninjuly.github.io/file_input.html'

        browser = webdriver.Chrome()
        browser.get(page_url)

        elements = browser.find_elements_by_css_selector('.form-group > input')
        for element in elements:
            element.send_keys('Answer')

        upload_file = browser.find_element_by_id('file')

        curr_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(curr_dir, 'input.txt')
        upload_file.send_keys(file_path)

        btn = browser.find_element_by_class_name('btn')
        btn.click()

    except Exception as e:
        print(e)
    finally:
        time.sleep(15)
        browser.quit()
