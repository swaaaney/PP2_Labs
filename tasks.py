import json

def json_file():
    data = {
        "product": "laptop",
        "price" : 1200,
        "brand" : "dell"
    }
    with open("data.json", "w") as file:
        json.dump(data, file)
json_file()

def read_json():
    with open("data.json", "r") as file:
        data = json.load()
        data["price"] = 900
    with open("data.json", "w") as file:
        json.dump(data, file)
read_json()