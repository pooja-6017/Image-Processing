import cv2 as c
import numpy as np
from matplotlib import pyplot as plt

i = c.imread("d:\python\g1.png", c.IMREAD_GRAYSCALE)
#i = c.cvtColor(i, c.COLOR_BGR2RGB) 

lp = c.Laplacian(i, c.CV_64F, ksize=3)
sobx = c.Sobel(i, c.CV_64F, 1, 0)
soby = c.Sobel(i, c.CV_64F, 0, 1)

sobx = np.uint8(np.absolute(sobx))
soby = np.uint8(np.absolute(soby))
lp = np.uint8(np.absolute(lp))

sobcombine = c.bitwise_or(sobx, soby)
title = ("Original", "Laplasian", "SobelX", "SobelY", "SobalCombine")
img = (i, lp, sobx, soby, sobcombine)

for i in range (5):
    plt.subplot(2, 3, i+1), plt.imshow(img[i], 'gray')
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])

plt.show()