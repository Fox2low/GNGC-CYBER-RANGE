import json


challenges_found = []
settings_file = "../Admin_Settings.json"

with open(settings_file, "r", encoding="utf-8") as f:
    settings = json.load(f)

    categories = settings.get('Categories')


    for category in categories:
        challenges_found.append(category)
    print(challenges_found)
    
