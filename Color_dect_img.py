import cv2 as c
import numpy as np
'''
i = c.imread("D:\python\g1.png")

while True:
    h = c.cvtColor(i, c.COLOR_BGR2HSV)
    i = c.resize(i, (400,400))

    u_val = np.array((26, 114, 247))
    l_val = np.array((0, 0, 121))

    #create mask
    masked =c.inRange(h, l_val, u_val)

    # filter
    res = c.bitwise_and(i, i, mask=masked)

    c.imshow("Original Grapes", i)
    c.imshow("Masking", masked)
    c.imshow("Result", res)

    if c.waitKey() & 0xFF == ord("x"):
        exit(0)
    c.destroyAllWindows()
'''

####Color detection using trackbar
i = c.imread("D:\\python\\g2.png")
#i = c.resize(i, (400,400))

def blend(x):
    pass

c.namedWindow("ColorDetection")

c.createTrackbar("l_h", "ColorDetection", 0, 255, blend)
c.createTrackbar("l_s", "ColorDetection", 0, 255, blend)
c.createTrackbar("l_v", "ColorDetection", 0, 255, blend)

c.createTrackbar("u_h", "ColorDetection", 255, 255, blend)
c.createTrackbar("u_s", "ColorDetection", 255, 255, blend)
c.createTrackbar("u_v", "ColorDetection", 255, 255, blend)

while True:
    hsv = c.cvtColor(i, c.COLOR_BGR2HSV)

    #get the value
    l_h = c.getTrackbarPos("l_h", "ColorDetection")
    l_s = c.getTrackbarPos("l_s", "ColorDetection")
    l_v = c.getTrackbarPos("l_v", "ColorDetection")

    u_h = c.getTrackbarPos("u_h", "ColorDetection")
    u_s = c.getTrackbarPos("u_s", "ColorDetection")
    u_v = c.getTrackbarPos("u_v", "ColorDetection")

    lower_val = np.array([l_h, l_s, l_v])
    upper_val = np.array([u_h, u_s, u_v])

    #create mask
    mask = c.inRange(hsv, lower_val, upper_val)

    #filter the mask
    res = c.bitwise_and(i, i, mask=mask)

    c.imshow("Original" ,i)
    c.imshow("Mask", mask)
    c.imshow("Result",res )

    #save images
    c.imwrite("D:\python\Output\Maskballcolor.jpg", mask)
    c.imwrite("D:\python\Output\Resultballcolor.jpg", res)

    if c.waitKey(1) & 0xFF == ord("x"):
        exit(0)
c.destroyAllWindows()

'''
####color detection using webcam
cap = c.VideoCapture(0)

def nothing(x):
    pass

c.namedWindow("Colordetection")

c.createTrackbar("l_h", "Colordetection", 0, 255, nothing)
c.createTrackbar("l_s", "Colordetection", 0, 255, nothing)
c.createTrackbar("l_v", "Colordetection", 0, 255, nothing)
c.createTrackbar("u_h", "Colordetection", 255, 255, nothing)
c.createTrackbar("u_s", "Colordetection", 255, 255, nothing)
c.createTrackbar("u_v", "Colordetection", 255, 255, nothing)

save = c.VideoWriter_fourcc(*'XVID')
output = c.VideoWriter("d\python\Output\color_detct_cam.mp4", save, 20.0, (400,400))

while True:
    _, f = cap.read()
    f = c.resize(f, (400,400))

    hsv = c.cvtColor(f, c.COLOR_BGR2HSV)
    
    l_h = c.getTrackbarPos("l_h", "Colordetection")
    l_s = c.getTrackbarPos("l_s", "Colordetection")
    l_v = c.getTrackbarPos("l_v", "Colordetection")

    u_h = c.getTrackbarPos("u_h", "Colordetection")
    u_s = c.getTrackbarPos("u_s", "Colordetection")
    u_v = c.getTrackbarPos("u_v", "Colordetection")

    l_val = np.array([l_h, l_s, l_v])
    u_val = np.array([u_h, u_s, u_v])

    mask = c.inRange(hsv, l_val, u_val)

    res = c.bitwise_and(f, f, mask=mask)

    c.imshow("Original", f)
    c.imshow("Mask", mask)
    c.imshow("Result", res)

    output.write(f)
    if c.waitKey(25) & 0xFF == ord("x"):
        exit(0)
    
cap.release()
c.destroyAllWindows()

# detect specific color using webcam
cap = c.VideoCapture(0)

while (cap.isOpened()):
    _, f= cap.read()
    h = c.cvtColor(f, c.COLOR_BGR2HSV)
    u_val = np.array((21,49,199))
    l_val = np.array((35,92,245))

    #create mask
    mask = c.inRange(h, l_val, u_val)

    # filter
    res = c.bitwise_and(f, f, mask=mask)

    c.imshow("Original", f)
    c.imshow("Masking", mask)
    c.imshow("Result", res)

    if c.waitKey() & 0xFF == ord("x"):
        exit(0)

cap.release()
c.destroyAllWindows()
'''