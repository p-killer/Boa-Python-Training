data = {
    "president": {
        "name": "Murthy",
        "city": "Hyderabad"
    }
}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)
