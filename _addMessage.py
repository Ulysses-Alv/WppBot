import json
import _generateID as gID

    
def addMessage(contactName, hour, minute, text, isOneTimeBool):
    with open("./database/automatizeMessage.json", "r") as f:
        autoJson = json.load(f)
    global newId
    newId = gID.generate()
    new_obj = {
        "name": contactName,
        "th": hour,
        "tm": minute,
        "message": text,
        "isOneTime": isOneTimeBool,
        "id": newId
    }
    autoJson['Gente'].append(new_obj)
    updated_json = json.dumps(autoJson)
    with open('./database/automatizeMessage.json', 'w') as f:
        f.write(updated_json)

