import json
    

def addMessage(contactName, birthday, text):
    with open("./database/cumples.json", "r") as f:
        birthdayJson = json.load(f)
    new_obj = {
        "name": contactName,
        "birthdate": birthday,
        "birthdayMessage": text
    }
    birthdayJson['Gente'].append(new_obj)
    updated_json = json.dumps(birthdayJson)
    with open('cumples.json', 'w') as f:
        f.write(updated_json)

