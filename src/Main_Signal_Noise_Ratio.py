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

def SNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if(mse == 0):  # MSE is zero means no noise is present in the signal .
                  # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr

if (originalImages and nearestNeighbourImages):
    for img in range(len(originalImages)):
        pathImage1 = pathOriginalSize+'/'+originalImages[img]
        pathImage2 = pathNearestNeighbour+'/'+nearestNeighbourImages[img]
        image1 = pil.open(pathImage1)
        image2 = pil.open(pathImage2)
        image1 = np.array(image1)
        image2 = np.array(image2)


