"""
Created on Sat Aug 31, 2019
@author: HyunsuKim6(Github), hyunsukim@kaist.ac.kr
"""

import os, random, shutil

train_size = 0.7

classes = []

for c in classes:

    files = [s for s in os.listdir(os.path.join(c))]
    random.shuffle(files)

    train_n = int(len(files) * train_size)
    train_files = files[0:train_n]

    folder_name = c + '_random'

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    for train_name in train_files:
        shutil.move(c + '\\' + train_name, folder_name)
