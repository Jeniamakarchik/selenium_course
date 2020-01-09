from selenium import webdriver
import time


if __name__ == "__main__":
    try:
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        name_field = browser.find_element_by_xpath(
            "//label[contains(text(), \"First name*\")]/following-sibling::input")
        last_field = browser.find_element_by_xpath(
            "//label[contains(text(), \"Last name*\")]/following-sibling::input")
        email_field = browser.find_element_by_xpath(
            "//label[contains(text(), \"Email*\")]/following-sibling::input")

        for field in [name_field, last_field, email_field]:
            field.send_keys("Answer")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        time.sleep(10)
        browser.quit()
