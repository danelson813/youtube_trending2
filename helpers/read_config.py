import json


def read_json():
    json_file = open("helpers/config.json")
    cfg = json.load(json_file)
    return cfg