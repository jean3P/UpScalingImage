from datetime import datetime

import cv2
import os

from UpScaling import UpScaling


# List the name of the images
def get_files(path):
    result = os.listdir(path)
    return result


originalPath = '../resources/original'
resizedNearestNeighbor = '../resources/nearestNeighbour'
resizedBilinearInterpolation = '../resources/bilinearInterpolation'

images = get_files(originalPath)

print("=== Statistics for the algorithm Nearest Neighbour ===")
for imgName in images:
    img = cv2.imread(originalPath + '/' + imgName)
    start_time = datetime.now()
    resizedImage = UpScaling.nearest_neighbour(img, 2)
    end_time = datetime.now()
    print(" === Imagen: ", imgName)
    print(' ===     Duration of Up-scaling: {} seconds'.format((end_time - start_time).total_seconds()))
    cv2.imwrite((resizedNearestNeighbor + '/' + imgName), resizedImage)

print(" ")
print(" ")

print("=== Statistics for the algorithm Bilineal Interpolation ===")
for imgName in images:
    img = cv2.imread(originalPath + '/' + imgName)
    start_time = datetime.now()
    resizedImage = UpScaling.bilinear_interpolation(img, 2)
    end_time = datetime.now()
    print(" === Imagen: ", imgName)
    print(' ===     Duration of Up-scaling: {} seconds'.format((end_time - start_time).total_seconds()))
    cv2.imwrite((resizedBilinearInterpolation + '/' + imgName), resizedImage)

print("*** All the images are scaling ***")