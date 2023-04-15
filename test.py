import os
import glob
import matplotlib.pyplot as plt
import cv2
import numpy as np

def plot(image_file, label_file):
    img = cv2.imread(image_file)
    with open(label_file, "r") as f:
        line = f.readline()

    tmp = line.strip().split(' ')

    w, h = img.shape[1], img.shape[0]
    x = [(float)(w.strip()) for w in tmp]

    x1 = int(x[1] * w)
    width = int(x[3] * w)

    y1 = int(x[2] * h)
    height = int(x[4] * h)
    print(x1, y1)
    print(width, height)
    img = cv2.rectangle(img, (x1 - width // 2, y1 - height // 2), (x1 + width // 2, y1 + height // 2), (255, 0, 0), 2)
    plt.imshow(img)
    plt.savefig('figure.png')
    plt.close('all')

plot('data_train/images/img_train_16.jpg',
         'data_train/labels/img_train_16.txt')
