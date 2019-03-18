import json

def parse_json(datas):
    for data in datas:
        print(data['image_host'])

with open('C:\\Workspace\\GoogleScrapping\\virtual_env\\scrapptest\\Scripts\\logs\\mimie mathy.json', 'r') as json_file:

    datas = json.loads(json_file.read())
    parse_json(datas)