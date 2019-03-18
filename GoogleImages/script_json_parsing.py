import json

def parse_json(datas):
    i = 1
    written_file = open("liste_des_urls", "w")
    for data in datas:
        written_file.write("{}".format(i) + '\n')
        written_file.write(data['image_host'] + '\n')
        written_file.write(data['image_link'] + '\n')
        written_file.write(data['image_source'] + '\n' + '\n')
        i = i+1

    written_file.close()

with open('C:\\Workspace\\GoogleScrapping\\virtual_env\\scrapptest\\Scripts\\logs\\mimie mathy.json', 'r') as json_file:

    datas = json.loads(json_file.read())
    parse_json(datas)