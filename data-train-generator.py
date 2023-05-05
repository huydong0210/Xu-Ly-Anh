import os
import glob
import matplotlib.pyplot as plt
import cv2
import numpy as np


def plot(image_path, label_path, bordered_image_path):
    img = cv2.imread(image_path)
    with open(label_path, "r") as f:
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
    plt.savefig(bordered_image_path)
    plt.close('all')


if __name__ == "__main__":
    old_root_images_path = 'data_train/images'
    old_root_labels_path = 'data_train/labels'
    new_root_images_path = 'new_data_train/images'
    new_root_labels_path = 'new_data_train/labels'
    list_images_name = os.listdir(new_root_images_path)
    list_labels_name = os.listdir(new_root_labels_path)

    for i in range(len(list_labels_name)):
        image_name = list_images_name.pop()
        label_name = list_labels_name.pop()
        new_image_path = new_root_images_path + '/' + image_name
        new_label_path = new_root_labels_path + '/' + label_name
        plot(new_image_path,new_label_path, 'after_plot' + '/' + image_name)