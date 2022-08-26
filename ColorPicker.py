import cv2 as c
import numpy as np
def cross(x):
    pass

i= np.zeros([300,512,3],np.uint8)
c.namedWindow("Color Picker")

S = "0:off\n1:on"
c.createTrackbar("S", "Color Picker", 0, 1, cross)
c.createTrackbar("B", "Color Picker", 0, 255, cross)
c.createTrackbar("G", "Color Picker", 0, 255, cross)
c.createTrackbar("R", "Color Picker", 0, 255, cross)

while True:
    c.imshow("Color Picker", i)
    if c.waitKey(1) & 0xFF == ord("x"):
        exit(0)

    s=c.getTrackbarPos("S", "Color Picker")
    r=c.getTrackbarPos("B", "Color Picker")
    g=c.getTrackbarPos("G", "Color Picker")
    b=c.getTrackbarPos("R", "Color Picker")

    if S==0:
        i[:]=0
    else:
        i[:]=[r,g,b]

c.destroyAllWindows()