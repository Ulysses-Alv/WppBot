import json


def deleteMessage(name):
    with open("./database/cumples.json", "r") as f:
        birthdayJson = json.load(f)

    data = birthdayJson
    name_to_find = name

    name_found = any(d['name'] == name_to_find for d in data['Gente'])

    if name_found:
        new_data = {
            "Gente": [item for item in data["Gente"] if item["name"] != name]}
        updated_json = json.dumps(new_data)
        with open('automatizeMessage.json', 'w') as f:
            f.write(updated_json)
        return name_found
    else:
        return name_found
