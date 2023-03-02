from datetime import datetime
from math import log10, sqrt

import PIL.Image as pil
import os

import numpy as np

from UpScaling import UpScaling


pathOriginalSize = '../resources/OriginalSize'
pathNearestNeighbour = '../resources/nearestNeighbour'

originalImages = os.listdir(pathOriginalSize)
nearestNeighbourImages = sorted(os.listdir(pathNearestNeighbour))

def signal_noise_ratio(original, compressed):
    pSignal = np.mean(original)
    pNoise = np.mean((original - compressed) ** 2)
    if(pNoise == 0):  # MSE is zero means no noise is present in the signal .
        return "Same Image"
    pNoise = sqrt(pNoise)
    # max_pixel = 255.0
    snr = 10 * log10(pSignal/pNoise)
    return snr

if (originalImages and nearestNeighbourImages):
    for img in range(len(originalImages)):
        pathImage1 = pathOriginalSize+'/'+originalImages[img]
        pathImage2 = pathNearestNeighbour+'/'+nearestNeighbourImages[img]
        image1 = pil.open(pathImage1)
        image2 = pil.open(pathImage2)
        image1 = np.array(image1)
        image2 = np.array(image2)

        print("Value SNR = ", signal_noise_ratio(image1, image2), "for the Image: ", originalImages[img])


