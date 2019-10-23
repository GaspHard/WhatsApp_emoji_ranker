#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 17:35:48 2019

@author: Gaspard
"""


import matplotlib
print('Default backend: ' + matplotlib.get_backend()) 
matplotlib.use("module://mplcairo.macosx")
print('Backend is now ' + matplotlib.get_backend())

import matplotlib.pyplot as plt
import re
from matplotlib.font_manager import FontProperties
#import numpy as np

f = open("discussion.txt","r")
content = f.readlines()
lVasi=[]
lLuc=[]
for x in content:
    if(x.find("Name1") != -1):
        lVasi.append(x)
    elif(x.find("Name2") != -1):
        lLuc.append(x)

strVasi = ''.join(lVasi)
strLuc = ''.join(lLuc)
exp = re.compile(u'([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
emoji_list_Vasi_raw = exp.findall(strVasi)
emoji_list_Luc_raw = exp.findall(strLuc)

emoji_list_Vasi = []
emoji_list_Luc = []
for l in emoji_list_Vasi_raw:
    emoji_list_Vasi.append(''.join(l))
    
for l in emoji_list_Luc_raw:
    emoji_list_Luc.append(''.join(l))

#print(emoji_list_Vasi)
#print("\n")
#print(emoji_list_Luc)

emoji_freq_Vasi = {}
emoji_freq_Luc = {}

for emoji in emoji_list_Vasi:
    if emoji in emoji_freq_Vasi:
        emoji_freq_Vasi[emoji] += 1
    else:
        emoji_freq_Vasi[emoji] = 1
        
for emoji in emoji_list_Luc:
    if emoji in emoji_freq_Luc:
        emoji_freq_Luc[emoji] += 1
    else:
        emoji_freq_Luc[emoji] = 1


for key in emoji_freq_Vasi.keys():
    emoji_freq_Vasi[key] = (emoji_freq_Vasi[key]/len(emoji_list_Vasi))*100
for key in emoji_freq_Luc.keys():
    emoji_freq_Luc[key] = (emoji_freq_Luc[key]/len(emoji_list_Luc))*100


emoji_freq_disp_Vasi = dict(sorted([(k,v) for k, v in emoji_freq_Vasi.items()], key = lambda x: x[1], reverse=True)[0:7])
emoji_freq_disp_Luc = dict(sorted([(k,v) for k, v in emoji_freq_Luc.items()], key = lambda x: x[1], reverse=True)[0:7])

print(emoji_freq_disp_Vasi)
print(emoji_freq_disp_Luc)   


prop = FontProperties(fname='/System/Library/Fonts/Apple Color Emoji.ttc')


fig, (vasi, luc) = plt.subplots(1, 2, figsize=(12, 6))
vasi.set_xticklabels(emoji_freq_disp_Vasi.keys(),fontproperties=prop,size=30)
luc.set_xticklabels(emoji_freq_disp_Luc.keys(),fontproperties=prop,size=30)
vasi.set_ylabel("Relative number of occurences (%)")
luc.set_ylabel("Relative number of occurences (%)")
luc.set_title("Him")
vasi.set_title("Her")
luc.bar(emoji_freq_disp_Luc.keys(), emoji_freq_disp_Luc.values(), color='blue')
vasi.bar(emoji_freq_disp_Vasi.keys(), emoji_freq_disp_Vasi.values(), color='pink')



        
        
f.close()

