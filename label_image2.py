import pandas as pd
import numpy as np
WS = pd.read_excel('Labels.xlsx')
labels = np.array(WS)
labels= labels[:,1:]
labels[0]
nans =np.nan_to_num(labels)

for r in range(labels.shape[0]):
    for c in range(labels.shape[1]):
        if labels[r][c] =='x':
            labels[r][c] = 1
        else:
            labels[r][c] = 0
        

labelsText = ['airplane','bare-soil','buildings','cars','chaparral','court','dock','field','grass','mobile-home','pavement','sand','sea',	'ship',	'tanks','trees','water']

alll= []


for i in range(labels.shape[0]):
    a = np.argwhere(labels[i] ==1)
    alll.append(a)

file
alll[1]
len(alll)
filelist = glob.glob('./images/*.txt')
filelist.sort()
filelist[0]
for i in range(len(filelist)):
    with open(filelist[i], 'a') as the_file:
        for j in alll[i]:
            the_file.write('\n'+labelsText[j[0]])

import os
os.chdir('/home/oguz/Downloads/begum_demir/UCMerced_LandUse/Multi-label-Inception-net-master')

with open('labels.txt', 'a') as the_file:
    for j in labelsText:
        the_file.write('\n'+j)
