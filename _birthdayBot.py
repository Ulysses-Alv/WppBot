import json
import _wppBot
import sys
import usageMemory
import time
import datetime

def sendBirthDayMessage(driver, contactName, birthdayText, birthday):
    dia_mes_actual = datetime.datetime.now().strftime("%d/%m")
    if birthday == dia_mes_actual:
        _wppBot.goToChat(driver, contactName)
        time.sleep(1)
        _wppBot.sendMessage(driver, birthdayText)
        time.sleep(1)
        
def main():
    with open("cumples.json", "r") as f:
        data = json.load(f)
    driver = _wppBot.openWhatsapp()
    for persona in data["Gente"]:
        _wppBot.sendBirthDayMessage(
            driver, persona["name"], persona["birthdayMessage"],  persona["birthdate"])
    usageMemory.printUsage()
    sys.exit()
        

if __name__ == '__main__':
    main()