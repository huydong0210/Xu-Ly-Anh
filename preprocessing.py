import cv2
import numpy as np
import os


def resize(image_path, size):
    old_img = cv2.imread(image_path)
    if (old_img.shape[0] > old_img.shape[1]):
        ratio = size[0] / old_img.shape[0]
    else:
        ratio = size[1] / old_img.shape[1]

    print(int(old_img.shape[0] * ratio), int(old_img.shape[1] * ratio))
    new_image = cv2.resize(old_img, (int(old_img.shape[1] * ratio), int(old_img.shape[0] * ratio)),
                           interpolation=cv2.INTER_AREA)
    return new_image


def padding(img, size):
    padded_img = cv2.copyMakeBorder(img, 0, size[0] - img.shape[0], 0, size[1] - img.shape[1], cv2.BORDER_CONSTANT,
                                    value=(255, 0, 0))
    return padded_img


def new_label(label_path, original_imgage):
    with open(label_path, "r") as f:
        line = f.readline()

    tmp = line.strip().split(' ')
    if original_imgage.shape[1] > original_imgage.shape[0]:
        index = original_imgage.shape[1]
    else:
        index = original_imgage.shape[0]
    tmp[1] = float(tmp[1]) * (original_imgage.shape[1] / index)
    tmp[2] = float(tmp[2]) * (original_imgage.shape[0] / index)
    tmp[3] = float(tmp[3]) * (original_imgage.shape[1] / index)
    tmp[4] = float(tmp[4]) * (original_imgage.shape[0] / index)
    result = str(tmp[0]) + ' ' + str(tmp[1]) + ' ' + str(tmp[2]) + ' ' + str(tmp[3]) + ' ' + str(tmp[4])
    return result


if __name__ == "__main__":
    # image_path = 'data_train/images/img_train_41.jpg'
    # label_path = 'data_train/labels/img_train_41.txt'
    # old_image = cv2.imread(image_path)
    # new_label(label_path, old_image)
    # cv2.imwrite('new_data_train/images/41.jpg', padding(resize(image_path, [640, 640]), [640, 640]))

    old_root_images_path = 'new_data_train/train/images'
    old_root_labels_path = 'new_data_train/train/labels'
    new_root_images_path = 'data_train_on_colab/images'
    new_root_labels_path = 'data_train_on_colab/labels'
    list_images_name = os.listdir(old_root_images_path)
    list_labels_name = os.listdir(old_root_labels_path)

    for i in range(len(list_labels_name)):
        image_name = list_images_name.pop()
        label_name = list_labels_name.pop()
        old_image_path = old_root_images_path + '/' + image_name
        old_label_path = old_root_labels_path + '/' + label_name
        old_image = cv2.imread(old_image_path)
        with open(new_root_labels_path + '/' + label_name, "w") as f:
            f.write(new_label(old_label_path, old_image))
        cv2.imwrite(new_root_images_path + '/' + image_name, padding(resize(old_image_path, [640, 640]), [640, 640]))


