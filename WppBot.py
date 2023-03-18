from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import os
import time
import math
import datetime
import argparse
import usageMemory
import json
import sys


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


def sendMessage(driver, birthdayText):
    textBox = driver.find_elements(By.CLASS_NAME, "iq0m558w")
    textBox[1].send_keys(birthdayText)


def goToChat(driver, contacto):
    xpath = '//span[@title="{}"]'.format(contacto)
    button = driver.find_element(By.XPATH, xpath)
    button.click()


def clickSend(driver):
    buttonSend = driver.find_element(
        By.CSS_SELECTOR, 'span[data-testid="send"]')
    buttonSend.click()


def sendBirthDayMessage(driver, contactName, birthdayText, birthday):
    dia_mes_actual = datetime.datetime.now().strftime("%d/%m")
    if birthday == dia_mes_actual:
        goToChat(driver, contactName)
        time.sleep(1)
        sendMessage(driver, birthdayText)
        time.sleep(1)
        clickSend(driver)


def main():
    with open("cumples.json", "r") as f:
        data = json.load(f)

        driver = openWhatsapp()
        for persona in data["Gente"]:
            sendBirthDayMessage(
                driver, persona["name"], persona["birthdayMessage"],  persona["birthdate"])
            usageMemory.printUsage()
            sys.exit()


if __name__ == '__main__':
    main()


"""""
    main_window = driver.current_window_handle

    while True:
        # comprueba si la ventana todavía está abierta
        if main_window not in driver.window_handles:
            # si la ventana ya no está abierta, detiene la ejecución del script
            sys.exit()
            
"""""
