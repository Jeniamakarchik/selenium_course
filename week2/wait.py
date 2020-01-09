from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


if __name__ == '__main__':
    try:
        page_url = 'http://suninjuly.github.io/explicit_wait2.html'

        browser = webdriver.Chrome()
        browser.get(page_url)

        WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
        )

        button = browser.find_element_by_id('book')
        button.click()

        x = int(browser.find_element_by_id('input_value').text)
        result = str(calc(x))

        input_field = browser.find_element_by_id('answer')
        browser.execute_script("return arguments[0].scrollIntoView(true);", input_field)
        input_field.send_keys(result)

        button = browser.find_element_by_id('solve')
        button.click()

        time.sleep(5)

    except Exception as e:
        print(e)

    finally:
        browser.quit()
