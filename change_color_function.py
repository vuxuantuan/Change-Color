import numpy as np


# change blue to gold
def change_blue_to_gold(img):
    img2 = np.zeros((img.shape[0], img.shape[1], 3))
    img2[:, :, 0] = img[:, :, 2]
    img2[:, :, 1] = img[:, :, 1]
    img2[:, :, 2] = img[:, :, 0]
    return img2


# change blue to green
def change_blue_to_green(img):
    img2 = np.zeros((img.shape[0], img.shape[1], 3))
    img2[:, :, 0] = (img[:, :, 0] + 255) / 2
    img2[:, :, 1] = img[:, :, 1]
    img2[:, :, 2] = img[:, :, 2] / 2
    return img2


# change blue to purple
def change_blue_to_purple(img):
    img2 = np.zeros((img.shape[0], img.shape[1], 3))
    img2[:, :, 0] = img[:, :, 1]
    img2[:, :, 1] = img[:, :, 1]
    img2[:, :, 2] = img[:, :, 0]
    return img2


# change blue to red
def change_blue_to_red(img):
    img2 = np.zeros((img.shape[0], img.shape[1], 3))
    img2[:, :, 0] = img[:, :, 1]
    img2[:, :, 1] = img[:, :, 1]
    img2[:, :, 2] = img[:, :, 0]
    return img2


# change purple to red
def change_purple_to_red(img):
    img2 = np.zeros((img.shape[0], img.shape[1], 3))
    img2[:, :, 0] = img[:, :, 2] * 2
    img2[:, :, 1] = img[:, :, 1]
    img2[:, :, 2] = img[:, :, 0] * 2
    return img2


# change purple to gray
def change_purple_to_gray(img):
    img2 = np.zeros((img.shape[0], img.shape[1], 3))
    img2[:, :, 0] = img[:, :, 0]
    img2[:, :, 1] = img[:, :, 2]
    img2[:, :, 2] = img[:, :, 1]
    return img2


# change purple to green
def change_purple_to_green(img):
    img2 = np.zeros((img.shape[0], img.shape[1], 3))
    img2[:, :, 0] = img[:, :, 2]
    img2[:, :, 1] = img[:, :, 1] * 2 - 255
    img2[:, :, 2] = img[:, :, 0]
    return img2


# change purple to gold
def change_purple_to_gold(img):
    img2 = np.zeros((img.shape[0], img.shape[1], 3))
    img2[:, :, 0] = img[:, :, 1]
    img2[:, :, 1] = img[:, :, 2] + 40
    img2[:, :, 2] = img[:, :, 0] + 40
    return img2


# change purple to blue
def change_purple_to_red(img):
    img2 = np.zeros((img.shape[0], img.shape[1], 3))
    img2[:, :, 0] = img[:, :, 0] * 3
    img2[:, :, 1] = img[:, :, 1]
    img2[:, :, 2] = img[:, :, 2] / 8
    return img2


# change gold to purple
def change_gold_to_purple(img):
    img2 = np.zeros((img.shape[0], img.shape[1], 3))
    img2[:, :, 0] = img[:, :, 2]
    img2[:, :, 1] = img[:, :, 0]
    img2[:, :, 2] = img[:, :, 1]
    return img2

# change gold to blue
def change_gold_to_blue(img):
    img2 = np.zeros((img.shape[0], img.shape[1], 3))
    img2[:, :, 0] = img[:, :, 2]
    img2[:, :, 1] = img[:, :, 0]
    img2[:, :, 2] = img[:, :, 0]
    return img2