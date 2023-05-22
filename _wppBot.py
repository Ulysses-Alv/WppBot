from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidArgumentException
import time
import _generateID as gID
from win10toast import ToastNotifier
import _deleteMessage as delete
import os
import pyautogui as pyt
contactIsArchivado = False

from PIL import ImageFile
import pyperclip
import base64

def copy_image_to_clipboard(image_path):
    
    with open(image_path, 'rb') as f:
        image_bytes = f.read()
    image_b64 = base64.b64encode(image_bytes).decode('utf-8')
    pyperclip.copy(image_b64)



def openWhatsapp():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=C:\\Path")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options)
        driver.get('https://web.whatsapp.com')
        driver.find_element
        assert 'WhatsApp' in driver.title
        # If your Wpp tooks too long to start, you should increase this value.
        time.sleep(25)
        return driver
    except InvalidArgumentException:
        print('ERROR: You may already have a Selenium navegator running in the background, close the window and run the code again, shutting down...')
        exit()


def goToAndSendMessage(driver, contacto, textOrImagePath):
    canContinue = True
    try:
        goToChat(driver, contacto)
    except:
        canContinue = False
        with open('failedLog.txt', 'a') as f:
            # If the contact name is not valid, the program will continue
            f.write("No existe: {}\n".format(contacto))
    if canContinue:
        sendMessage(driver, textOrImagePath)
        toastNotifier(contacto)
        time.sleep(1)


def deleteIf(isOneTime, id):
    if isOneTime:
        delete.deleteMessageById(id)


def toastNotifier(contacto):
    ruta_icono = "./icon/whatsapp.ico"
    toaster = ToastNotifier()
    toaster.show_toast("Mensaje Enviado", "Mensaje enviado a {} correctamente".format(
        contacto), icon_path=ruta_icono)


def goToChat(driver, contacto):
    try:
        xpath = '//span[@title="{}"]'.format(contacto)
        button = driver.find_element(By.XPATH, xpath)
        button.click()
    except:
        goToArchivados(driver)
        xpath = '//span[@title="{}"]'.format(contacto)
        button = driver.find_element(By.XPATH, xpath)
        button.click()


def goToArchivados(driver):
    global contactIsArchivado
    xpath = '//div[text()="Archivados"]'
    button = driver.find_element(By.XPATH, xpath)
    button.click()
    contactIsArchivado = True
    time.sleep(1)


def sendMessage(driver, textOrImage):
    global contactIsArchivado
    if os.path.exists(textOrImage):
        copy_image_to_clipboard(textOrImage)
        pyt.hotkey('ctrl', 'v')
    else:
        textBox = driver.find_elements(By.CLASS_NAME, "iq0m558w")
        textBox[1].send_keys(textOrImage)
    clickSend(driver)
    if contactIsArchivado:
        goBack(driver)


def goBack(driver):
    buttonGoBack = driver.find_elements(
        By.CSS_SELECTOR, 'span[data-testid="back"]')
    buttonGoBack[0].click()


def clickSend(driver):
    buttonSend = driver.find_element(
        By.CSS_SELECTOR, 'span[data-testid="send"]')
    buttonSend.click()
