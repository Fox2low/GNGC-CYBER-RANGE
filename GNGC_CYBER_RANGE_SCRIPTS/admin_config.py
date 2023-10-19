import json
import challenge_info

#Adds chanllange to json file
def update_json(name):
    file_path = "../Admin_Config.json"
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        data = {}

    if 'challenges' not in data:
        data['challenges'] = {}

    data['challenges'][name] = {
        "Viewable": "True",
        "Enabled": "False",
        "Data": "NULL"
    }
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


#Updates the challanges with the default settings
def update_challanges():
    for i in challenge_info.get_category():
        names = challenge_info.get_challenges(i)
        for x in names:
            update_json(x)
    return True

def update_data(challenge, key, Data):
    file_path = "../Admin_Config.json"
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        data = {}
    if 'challenges' not in data:
        data['challenges'] = {}

    if challenge in data['challenges']:
        data['challenges'][challenge][key] = Data

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    else:
        return "Error challenge not found!"
    return "True"


def get_data(challenge):
    file_path = "../Admin_Config.json"
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
                data = {}
    if 'challenges' not in data:
        return "File Empty!"
    if challenge in data['challenges']:
        return data['challenges'][challenge]


update_challanges()
print(get_data("How Helpful"))
update_data("How Helpful", "Viewable", "False")
print(get_data("How Helpful"))