import json


def deleteMessageByName(name, nameOfJson):
    with open(nameOfJson, "r") as f:
        data = json.load(f)

    name_to_find = name

    name_found = any(d['name'] == name_to_find for d in data['Gente'])

    if name_found:
        new_data = {
            "Gente": [item for item in data["Gente"] if item["name"] != name]}
        updated_json = json.dumps(new_data)
        with open(nameOfJson, 'w') as f:
            f.write(updated_json)
        return name_found
    else:
        return name_found


def deleteMessageById(id, nameOfJson):
    with open(nameOfJson, "r") as f:
        data = json.load(f)

    id_to_find = id

    id_found = any(data['id'] == id_to_find for data in data['Gente'])

    if id_found:
        new_data = {
            "Gente": [item for item in data["Gente"] if item["id"] != id]}
        updated_json = json.dumps(new_data)
        with open(nameOfJson, 'w') as f:
            f.write(updated_json)
        return id_found
    else:
        return id_found
