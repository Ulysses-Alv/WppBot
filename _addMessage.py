import json

with open("automatizeMessage.json", "r") as f:
    autoJson = json.load(f)
    
def addMessage(contactName, hour, minute, text):
    new_obj = {
        "name": contactName,
        "th": hour,
        "tm": minute,
        "message": text
    }
    autoJson['Gente'].append(new_obj)
    updated_json = json.dumps(autoJson)
    with open('automatizeMessage.json', 'w') as f:
        f.write(updated_json)

