import os

from PIL import Image

import numpy as np

pathOriginalSize = '../resources/OriginalSize'
pathNearestNeighbour = '../resources/nearestNeighbour'

originalImages = os.listdir(pathOriginalSize)
nearestNeighbourImages = sorted(os.listdir(pathNearestNeighbour))
if (originalImages and nearestNeighbourImages):
    for img in range(len(originalImages)):
        pathImage1 = pathOriginalSize+'/'+originalImages[img]
        pathImage2 = pathNearestNeighbour+'/'+nearestNeighbourImages[img]
        image1 = Image.open(pathImage1)
        image2 = Image.open(pathImage2)

        buffer1 = np.asarray(image1)
        buffer2 = np.asarray(image2)

        buffer3 = buffer1 - buffer2

        # buffer4 = buffer3 - buffer1

        # Construct a new Image from the resultant buffer
        differenceImage = Image.fromarray(buffer3);

        # Display all the images including the difference image

        # image1.show();

        # image2.show();

        differenceImage.show();
