# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 15:54:04 2021

@author: zsd
"""

import os

path = 'C:\\Users\\zsd\\Downloads\\skybox\\'

res = '8192 4096'
form = 'JPEG'
blender_path = 'C:\\Program Files\\Blender Foundation\\Blender 2.83\\blender.exe'
output = path+'out'

for i in range(78,116): 
    front = path+'pano'+str(i)+'_skybox3.jpg'
    back = path+'pano'+str(i)+'_skybox1.jpg'
    left = path+'pano'+str(i)+'_skybox2.jpg'
    right = path+'pano'+str(i)+'_skybox4.jpg'
    top = path+'pano'+str(i)+'_skybox0.jpg'
    bottom = path+'pano'+str(i)+'_skybox5.jpg'
    
    
    cmd = 'cube2sphere '+front+' '+back+' '+left+' '+right+' '+top+' '+bottom+' -r '+res+' -f'+form+' -o "'+output+'" -b "'+blender_path+'"'
    # cmd = 'cube2sphere pano0_skybox3.jpg pano0_skybox1.jpg pano0_skybox2.jpg pano0_skybox4.jpg pano0_skybox0.jpg pano0_skybox5.jpg -r 8192 4096 -fJPEG -opano -b "C:\Program Files\Blender Foundation\Blender 2.83\blender.exe"'
    os.system(cmd)
    os.rename(output+'0001.jpg',path+'panos\\pano'+str(i)+'.jpg')
    print('pano'+str(i))