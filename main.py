import csv
import os
import cv2
import numpy as np
import pandas as pd


width = 850
height = 1050
path = 'manga/qwferweqw.jpg'
img = cv2.imread(path)
img = cv2.resize(img, (width, height))
imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
savepath = 'C:/Users/Asus/Downloads/manga-translator/thres/1.png'
savepath2 = 'C:/Users/Asus/Downloads/manga-translator/thres/2.png'
cv2.imwrite(savepath,imggray)
#kernel = np.ones((5,5),np.uint8)
#imggray= cv2.morphologyEx(imggray, cv2.MORPH_TOPHAT, kernel)
kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
imggray = cv2.filter2D(imggray, -1, kernel)

cmd='python detect.py --source C:/Users/Asus/Downloads/manga-translator/thres/1.png --weights runs/train/yolov5s_results4/weights/best.pt --conf 0.4'
os.system(cmd)
data = pd.read_csv("GFG.csv")
arr = data.to_numpy()
j = arr.tolist()
x=0
res = []
if len(j)<2:
    for x in list(j)[0][1:5]:
        res.append(x)
elif len(j)>=2:
    for x in list(j):
        for y in list(x)[1:5]:
            res.append(y)
#print(res)
b = int(len(res) / 4)
i = 0
for i in range(b):
    n = int(i * 4 + 1)
    croped_img = imggray[int(res[int(n)]):int(res[int(n + 2)]), int(res[int(n - 1)]):int(res[int(n + 1)])]
    #croped_img = cv2.cvtColor(croped_img, cv2.COLOR_BGR2GRAY)

    if i == 0:
        shape = croped_img.shape
        #print(shape)
        pppp = np.zeros((shape[0] * b, shape[1])).astype('uint8')
        pppp[shape[0] * (i):shape[0] * (i + 1), :] = croped_img
    else:
        croped_img = cv2.resize(croped_img, (shape[1], shape[0]))
        cv2.imshow('bine',croped_img)
        cv2.imwrite(savepath2,croped_img)
        pppp[shape[0] * (i):shape[0] * (i + 1), :] = croped_img
