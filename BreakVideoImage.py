#break the video in image
import cv2 as c

vcap =c.VideoCapture(0)
ret, im = vcap.read()
count = 0

while True:
    if ret == True:
        c.imwrite("D:\python\Output\V_Image\Image_%d.jpg "%count,im)
        vcap.set(c.CAP_PROP_POS_MSEC,(count**10))
        ret, im = vcap.read()
        c.imshow("V_Br_Image", im)

        count += 1
        if c.waitKey(1) & 0xFF == ord('x'):
            exit(0)
            c.destroyAllWindows()

vcap.release()
c.destroyAllWindows()