import json

def load_user_data():
    with open("data/user_data.json") as f:
        return json.load(f)