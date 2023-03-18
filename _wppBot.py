from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidArgumentException
import time

def openWhatsapp():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=C:\\Path")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options)
        driver.get('https://web.whatsapp.com')
        assert 'WhatsApp' in driver.title
        time.sleep(15)

        return driver

    except InvalidArgumentException:
        print('ERROR: You may already have a Selenium navegator running in the background, close the window and run the code again, shutting down...')
        exit()

def goToChat(driver, contacto):
    xpath = '//span[@title="{}"]'.format(contacto)
    button = driver.find_element(By.XPATH, xpath)
    button.click()

def sendMessage(driver, text):
    textBox = driver.find_elements(By.CLASS_NAME, "iq0m558w")
    textBox[1].send_keys(text)
    clickSend(driver)


def clickSend(driver):
    buttonSend = driver.find_element(
        By.CSS_SELECTOR, 'span[data-testid="send"]')
    buttonSend.click()