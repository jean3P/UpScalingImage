import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../resources/aef-CSN-III-3-1_088-300x450.jpg')
print(type(img))
print(img.shape[0], img.shape[1])

cv2.imshow('Figure',img)
cv2.waitKey()