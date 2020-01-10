import time
import math

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


urls = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]
@pytest.mark.parametrize('url', urls)
def test_stepik(browser, url):
    browser.get(url)

    text_field = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.TAG_NAME, 'textarea'))
    )
    browser.execute_script("return arguments[0].scrollIntoView(true);", text_field)
    text_field.send_keys(str(math.log(int(time.time()))))

    button = browser.find_element_by_tag_name('button')
    button.click()

    text = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.TAG_NAME, 'pre'))
    ).text
    assert text == 'Correct!', f'Text: {text}'
