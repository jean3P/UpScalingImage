import os
from math import log10, sqrt

from PIL import Image, ImageChops

import numpy as np

pathOriginalSize = '../resources/OriginalSize'
pathNearestNeighbour = '../resources/nearestNeighbour'
pathBilinearInterpolation = '../resources/bilinearInterpolation'
pathSubtractionNormal = '../resources/subtraction/normal'
pathSubtractionSecond = '../resources/subtraction/second'

def statistics_image2_greater_than_image1(image, image2):
    list = np.greater(image2, image)
    num = list.sum()
    size = image1.size
    size = size[0] * size[1] * 3
    total = (num * 100) / size
    return total


def statistics_image1_equal_image2(image, image2):
    list = np.equal(image2, image)
    num = list.sum()
    size = image1.size
    size = size[0] * size[1] * 3
    total = (num * 100) / size
    return total


def statistics_image1_greater_than_image2(image, image2):
    list = np.greater(image, image2)
    num = list.sum()
    size = image1.size
    size = size[0] * size[1] * 3
    total = (num * 100) / size
    return total


def normal_subtract(image1, image2):
    return (image1 - image2)


def only_subtract_when_image1_is_greater_than_image2(image1, image2):
    return ImageChops.subtract(image1, image2)


def open_image(path, name):
    path_image = path + '/' + name
    return Image.open(path_image)


def print_statistics(buffer1, buffer2):
    print("Image Size: ", buffer1.shape[1], "X", buffer1.shape[0])
    print(" === Stadistics ===")
    print("     Equal pixels in both images (%): ", round(statistics_image1_equal_image2(buffer1, buffer2), 2))
    print("     Number of pixels of the original image that are greater than the scaled  (%): ",
          round(statistics_image1_greater_than_image2(buffer1, buffer2), 2))
    print("     Number of pixels of the scaled image that are greater than the original image (%): ",
          round(statistics_image2_greater_than_image1(buffer1, buffer2), 2))

def signal_noise_ratio(original, compressed):
    pSignal = np.mean(original)
    pNoise = np.mean((original - compressed) ** 2)
    if (pNoise == 0):  # is zero means no noise is present in the signal .
        return "Same Image"
    pNoise = sqrt(pNoise)
    # print(pSignal)
    # print(pNoise)
    snr = 10 * log10(pSignal / pNoise)
    return snr


def print_statistics_nsr(image1, image2, name):
    print("Value SNR = ", signal_noise_ratio(image1, image2), "dB. for the Image: ", name)

originalImages = os.listdir(pathOriginalSize)
nearestNeighbourImages = sorted(os.listdir(pathNearestNeighbour))
bilinealInterpolationImages = sorted(os.listdir(pathBilinearInterpolation))


if originalImages and nearestNeighbourImages and bilinealInterpolationImages:
    print(" ==== Nearest Neighbour ==== ")
    for img in range(len(originalImages)):

        image1 = open_image(pathOriginalSize, originalImages[img])
        buffer1 = np.asarray(image1)

        image2 = open_image(pathNearestNeighbour, nearestNeighbourImages[img])
        buffer2 = np.asarray(image2)

        buffer3 = normal_subtract(buffer1, buffer2)
        print_statistics(buffer1, buffer2)
        differenceImage = Image.fromarray(buffer3)
        differenceImage.save(pathSubtractionNormal + '/' + 'nearestNeighbour/' + originalImages[img])
        image3 = only_subtract_when_image1_is_greater_than_image2(image1, image2)
        print_statistics_nsr(buffer1, buffer2, originalImages[img])
        # differenceImage.show()
        # image3.show()
        image3.save(pathSubtractionSecond + '/' + 'nearestNeighbour/' + originalImages[img])

    print(" ==== Bilineal Interpolation ==== ")
    for img in range(len(originalImages)):
        image1 = open_image(pathOriginalSize, originalImages[img])
        buffer1 = np.asarray(image1)

        image2 = open_image(pathBilinearInterpolation, bilinealInterpolationImages[img])
        buffer2 = np.asarray(image2)

        buffer3 = normal_subtract(buffer1, buffer2)
        print_statistics(buffer1, buffer2)
        differenceImage = Image.fromarray(buffer3)
        differenceImage.save(pathSubtractionNormal + '/' + 'bilinealInterpolation/' + originalImages[img])
        image3 = only_subtract_when_image1_is_greater_than_image2(image1, image2)
        print_statistics_nsr(buffer1, buffer2, originalImages[img])

        image3.save(pathSubtractionSecond + '/' + 'bilinealInterpolation/' + originalImages[img])

