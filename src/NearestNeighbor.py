import numpy as np


class NearestNeighbor:

    @staticmethod
    def run(image):
        Factor = 2
        originalWidth, originalHeight, channel = image.shape
        redChannel = image[:, :, 0]
        greenChannel = image[:, :, 1]
        blueChannel = image[:, :, 2]

        resizeWidth = originalWidth*Factor
        resizeHeight = originalHeight*Factor

        resizedImage = np.zeros((resizeWidth, resizeHeight, channel), dtype=np.uint8)

        xRatio = originalWidth/resizeWidth
        yRatio = originalHeight/resizeHeight

        resizeIndexX = np.ceil(np.arange(0, originalWidth, xRatio)).astype(int)
        resizeIndexY = np.ceil(np.arange(0, originalHeight, yRatio)).astype(int)

        resizeIndexX[np.where(resizeIndexX == originalWidth)] -= 1
        resizeIndexY[np.where(resizeIndexY == originalHeight)] -= 1

        resizedImage[:, :, 0] = redChannel[resizeIndexX, :][:, resizeIndexY]
        resizedImage[:, :, 1] = greenChannel[resizeIndexX, :][:, resizeIndexY]
        resizedImage[:, :, 2] = blueChannel[resizeIndexX, :][:, resizeIndexY]

        return resizedImage

