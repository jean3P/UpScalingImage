import math

import numpy as np


class UpScaling:

    @staticmethod
    def nearest_neighbour(image, factor):
        # Extract the dimensions of the image
        originalHeight, originalWidth, channel = image.shape

        # Get the values of each channel
        redChannel = image[:, :, 0]
        greenChannel = image[:, :, 1]
        blueChannel = image[:, :, 2]

        # The new dimensions of the scaled image are calculated (taking into account the factor)
        resizeWidth = originalWidth*factor
        resizeHeight = originalHeight*factor

        # A new array of zeros with the new dimensions is created.
        resizedImage = np.zeros((resizeHeight, resizeWidth , channel), dtype=np.uint8)

        # The information needed by the Nearest neighbour are the ratios
        # (vertical and horizontal) between the original image and the new image.
        xRatio = originalWidth/resizeWidth if resizeWidth != 0 else 0
        yRatio = originalHeight/resizeHeight if resizeHeight != 0 else 0

        # The arange function is used to create two new arrays from 0 to the original dimension
        #   (originalWidth, originalHeight), with spaces in between (xRatio and yRatio).
        # The ceil function allows me to round a number to the nearest integer.
        resizeIndexX = np.ceil(np.arange(0, originalWidth, xRatio)).astype(int)
        resizeIndexY = np.ceil(np.arange(0, originalHeight, yRatio)).astype(int)

        # The last value is subtracted by one to avoid going out of range
        resizeIndexX[np.where(resizeIndexX == originalWidth)] -= 1
        resizeIndexY[np.where(resizeIndexY == originalHeight)] -= 1

        # After creating the arrays with the new nearest new positions,
        # their value is retrieved and the new resized image is created.
        resizedImage[:, :, 0] = redChannel[resizeIndexY, :][:, resizeIndexX]
        resizedImage[:, :, 1] = greenChannel[resizeIndexY, :][:, resizeIndexX]
        resizedImage[:, :, 2] = blueChannel[resizeIndexY, :][:, resizeIndexX]

        return resizedImage

    @staticmethod
    def bilinear_interpolation(image, factor):
        # Extract the dimensions of the image
        originalHeight, originalWidth, channel = image.shape

        # The new dimensions of the scaled image are calculated (taking into account the factor)
        resizeWidth = originalWidth*factor
        resizeHeight = originalHeight*factor

        # A new array of zeros with the new dimensions is created.
        resizedImage = np.zeros((resizeHeight, resizeWidth, channel), dtype=np.uint8)

        # The information needed are the ratios (vertical and horizontal) between the original image and the new image.
        widthRatio = originalWidth/resizeWidth if resizeWidth != 0 else 0
        heightRatio = originalHeight/resizeHeight if resizeHeight != 0 else 0

        for i in range(resizeHeight):
            for j in range(resizeWidth):
                # map the coordinates back to the original image.
                x = i * heightRatio
                y = j * widthRatio
                # calculate the coordinate values for 4 surrounding pixels.
                x_floor = math.floor(x)
                x_ceil = min(originalHeight - 1, math.ceil(x))
                y_floor = math.floor(y)
                y_ceil = min(originalWidth - 1, math.ceil(y))

                # When both x and y have integers values, means that the coordinates of a pixel in the resized image
                # coincide with a particular pixel of the original image. In this case is not necessary estimate the
                # pixel value.
                if (x_ceil == x_floor) and (y_ceil == y_floor):
                    q = image[int(x), int(y), :]

                #  When either one of them is an integer, the bilinear interpolation turns into linear interpolation.
                elif x_ceil == x_floor:
                    q1 = image[int(x), int(y_floor), :]
                    q2 = image[int(x), int(y_ceil), :]
                    q = q1 * (y_ceil - y) + q2 * (y - y_floor)
                elif y_ceil == y_floor:
                    q1 = image[int(x_floor), int(y), :]
                    q2 = image[int(x_ceil), int(y), :]
                    q = (q1 * (x_ceil - x)) + (q2 * (x - x_floor))
                else:
                    # we get the neighbouring pixel values
                    v1 = image[x_floor, y_floor, :]
                    v2 = image[x_ceil, y_floor, :]
                    v3 = image[x_floor, y_ceil, :]
                    v4 = image[x_ceil, y_ceil, :]
                    # Estimate the pixel value q using pixel values of neighbours
                    q1 = v1 * (x_ceil - x) + v2 * (x - x_floor)
                    q2 = v3 * (x_ceil - x) + v4 * (x - x_floor)
                    q = q1 * (y_ceil - y) + q2 * (y - y_floor)
                resizedImage[i, j, :] = q
        return resizedImage

