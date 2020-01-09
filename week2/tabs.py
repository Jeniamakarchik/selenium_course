from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


if __name__ == '__main__':
    try:
        page_url = 'http://suninjuly.github.io/redirect_accept.html'

        browser = webdriver.Chrome()
        browser.get(page_url)

        btn = browser.find_element_by_tag_name('button')
        btn.click()

        browser.switch_to.window(browser.window_handles[1])

        x = int(browser.find_element_by_id('input_value').text)
        result = calc(x)

        input_field = browser.find_element_by_id('answer')
        input_field.send_keys(str(result))

        btn = browser.find_element_by_class_name('btn')
        btn.click()

        time.sleep(15)

    except Exception as e:
        print(e)

    finally:
        browser.quit()
