# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 15:05:42 2021

@author: zsd
"""

import json
import requests

with open("data.json", "r") as read_file:
    data = json.load(read_file)
    
    for i in range(105,len(data['data']['model']['locations'])):
        pano = data['data']['model']['locations'][i]['panos'][0]
        id = pano['id']
        
        pos_x = pano['position']['x']
        pos_y = pano['position']['y']
        pos_z = pano['position']['z']
        
        rot_x = pano['rotation']['x']
        rot_y = pano['rotation']['y']
        rot_z = pano['rotation']['z']
        rot_w = pano['rotation']['w']
        
        skybox = pano['skybox']['children']
        
        for j in range(len(skybox)):
            url = skybox[j]
            r = requests.get(url)
            name = 'skybox/pano'+str(i)+'_skybox'+str(j)+'.jpg'
            print(name)
            open(name, 'wb').write(r.content)
    

    