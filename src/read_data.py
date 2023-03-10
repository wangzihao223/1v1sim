import json
def read_data(file):
    with open('./config.json', 'r') as f:
        data = json.loads(file)
        return data
