import time
import json
import _wppBot

timeToSendHour = ""
contactName = ""
timeToSendMinute = ""
message = ""
data = []
driver = ""

with open("automatizeMessage.json", "r") as f:
    data = json.load(f)
    
def getPersona(persona) : 
    global timeToSendHour
    global contactName
    global timeToSendMinute
    global message
    global data
    contactName = data["Gente"][persona]["name"]
    timeToSendHour = data["Gente"][persona]["th"]
    timeToSendMinute = data["Gente"][persona]["tm"]
    message = data["Gente"][persona]["message"]
    
def getDriver() :
    global driver
    if driver == "" :
        driver = _wppBot.openWhatsapp()

def onTimeSender() :
    global driver
    getDriver()
    _wppBot.goToChat(driver, contactName)
    _wppBot.sendMessage(driver, message)
    time.sleep(5)

while True : 
    hora_local = time.localtime()
    for index, persona in enumerate(data["Gente"]) :
        if str(hora_local.tm_hour) == persona["th"] and str(hora_local.tm_min) == persona["tm"] :
            getPersona(index)
            onTimeSender()
            time.sleep(3)
    try:
        driver.close()
        time.sleep(60)
    except AttributeError :
        time.sleep(60)
    