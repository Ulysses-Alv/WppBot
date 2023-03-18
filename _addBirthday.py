import json
    
with open("cumples.json", "r") as f:
    birthdayJson = json.load(f)

def addMessage(contactName, birthday, text):
    new_obj = {
        "name": contactName,
        "birthdate": birthday,
        "birthdayMessage": text
    }
    birthdayJson['Gente'].append(new_obj)
    updated_json = json.dumps(birthdayJson)
    with open('cumples.json', 'w') as f:
        f.write(updated_json)

