import time
import json
import _wppBot as wpp
from win10toast import ToastNotifier

timeToSendHour = ""
contactName = ""
timeToSendMinute = ""
message = ""
isOneTime = ""
id = ""
data = []
driver = ""

with open("./database/automatizeMessage.json", "r") as f:
    data = json.load(f)


def getPersona(persona):
    global timeToSendHour
    global contactName
    global timeToSendMinute
    global message
    global data
    global isOneTime
    global id
    contactName = data["Gente"][persona]["name"]
    timeToSendHour = data["Gente"][persona]["th"]
    timeToSendMinute = data["Gente"][persona]["tm"]
    message = data["Gente"][persona]["message"]
    isOneTime = data["Gente"][persona]["isOneTime"]
    id = data["Gente"][persona]["id"]


def getDriver():
    global driver
    if driver == "":
        driver = wpp.openWhatsapp()


def onTimeSender():
    global driver
    getDriver()
    wpp.goToAndSendMessage(driver, contactName, message)
    wpp.deleteIf(isOneTime, id)


toaster = ToastNotifier()
ruta_icono = "./icon/whatsapp.ico"
toaster.show_toast("Se Inició", "onTimeSender.py iniciado",
                   icon_path=ruta_icono)
while True:
    hora_local = time.localtime()
    for index, persona in enumerate(data["Gente"]):
        isSameTime = hora_local.tm_hour == persona["th"] and hora_local.tm_min == persona["tm"]
        if isSameTime:
            getPersona(index)
            onTimeSender()
            time.sleep(2)
    try:
        driver.close()
        time.sleep(30)
    except:
        time.sleep(30)
