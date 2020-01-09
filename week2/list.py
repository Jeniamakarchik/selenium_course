from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time


if __name__ == '__main__':
    try:
        page_url = 'http://suninjuly.github.io/selects2.html'

        browser = webdriver.Chrome()
        browser.get(page_url)

        x = int(browser.find_element_by_id('num1').text)
        y = int(browser.find_element_by_id('num2').text)
        result = str(x + y)

        select = Select(browser.find_element_by_tag_name('select'))
        select.select_by_value(result)

        btn = browser.find_element_by_class_name('btn')
        btn.click()
    except Exception as e:
        print(e)
    finally:
        time.sleep(15)
        browser.quit()
