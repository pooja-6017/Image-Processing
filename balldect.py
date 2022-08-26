# Extract color of ball from an image
'''
import cv2 as c
import numpy as np

i = c.imread("D:\python\g1.png")

while(True):
    hsv = c.cvtColor(i, c.COLOR_BGR2HSV)
    l_v = np.array((0, 5, 151))
    u_v = np.array((26, 109, 245))

    mask = c.inRange(hsv, l_v, u_v)
    res = c.bitwise_and(i, i, mask=mask)

    c.imshow("Grapes", i)
    #c.imshow("Mask", mask)
    c.imshow("Result", res)

    if c.waitKey() == ord('x'):
        exit(0);

c.destroyAllWindows()
'''
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2
from collections import Counter
from skimage.color import rgb2lab,deltaE_cie76
import os

#RGB To HEX Conversion
def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))



#Get color function
def get_colors(image,number_of_colors,show_chart):
    modified_image = cv2.resize(image, (600, 400), interpolation = cv2.INTER_AREA)
    modified_image = modified_image.reshape(modified_image.shape[0]*modified_image.shape[1], 3)
    clf = KMeans(n_clusters = number_of_colors)
    labels = clf.fit_predict(modified_image)
    counts = Counter(labels)
    center_colors = clf.cluster_centers_
    # We get ordered colors by iterating through the keys
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
    rgb_colors = [ordered_colors[i] for i in counts.keys()]

    if (show_chart):
        plt.figure(figsize = (8, 6))
        plt.pie(counts.values(), labels = hex_colors, colors = hex_colors)
        plt.legend(title = "Dominant colors in Image")


    return rgb_colors


img = cv2.imread("D:\python\g2.png")

if img is None:
    print("Incorrect path! Image not found")

else:
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    fig = plt.figure(figsize=(3,7))
    ax = fig.add_subplot(111)
    ax.imshow(img)
    get_colors(img,8,True)