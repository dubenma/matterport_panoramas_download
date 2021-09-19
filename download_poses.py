import csv
import json
import os.path
import requests
from requests.auth import HTTPBasicAuth
  
path = r'C:\Users\zsd\CIIRC\data\matterport\Broca Hospital without Curtains'
space_id = '6ak4XqnRK9c'

matterport_id = ''
secret_token = ''
  
url = 'https://api.matterport.com/api/models/graph?query=query{model(id:"'+space_id+'"){locations{panos{id%20position{x%20y%20z}%20rotation{x%20y%20z%20w}%20skybox(resolution:"2k"){children}}}}}'
response = requests.get(url,
            auth = HTTPBasicAuth(matterport_id, secret_token))

data = json.loads(response.text)
l = len(data['data']['model']['locations'])

with open(os.path.join(path,'poses.csv'), 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')

    for i in range(l):
        pano = data['data']['model']['locations'][i]['panos'][0]
        
        pos_x = pano['position']['x']
        pos_y = pano['position']['y']
        pos_z = pano['position']['z']
        
        rot_x = pano['rotation']['x']
        rot_y = pano['rotation']['y']
        rot_z = pano['rotation']['z']
        rot_w = pano['rotation']['w']
        
        row = [pos_x, pos_y, pos_z, rot_x, rot_y, rot_z, rot_w]
        
        spamwriter.writerow(row)

