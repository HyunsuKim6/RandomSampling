"""
Created on Sat Aug 31, 2019
@author: HyunsuKim6(Github), hyunsukim@kaist.ac.kr
"""

import cv2
import os

cap = cv2.VideoCapture()

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0

while(True):

    ret, frame = cap.read("")

    if not ret: break

    name = './data/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    currentFrame += 1

dirname = r""
filenames = os.listdir(dirname)

try:
    if not os.path.exists('Result'):
        os.makedirs('Result')
except OSError:
    print ('Error: Creating directory of data')

for filename in filenames:
    img = cv2.imread(dirname + "\\" + filename)
    x = 448; y = 88;
    w = 1024; h = 1024;
    img_tilled = img[int(y): int(y + h), int(x): int(x + w)]
    path = r""
    name = './Result' + "/" + filename
    cv2.imwrite(path + "\\" + filename, img_tilled)
    print("Tiling..." + name)

cap.release()
cv2.destroyAllWindows()