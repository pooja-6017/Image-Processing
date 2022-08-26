import cv2 as c
import numpy as np
import datetime as dt
'''
# Drawing on IMAGE
img = c.imread("D:\python\landscape.jpg")
img = c.resize(img, (950,700))
#img = np.zeros([500, 500, 3], np.uint8)*155
#img = np.ones([500, 500, 3], np.uint8)*255

img = c.line(img, (50,50), (50,200), (136, 252, 3), 3)              # line
img = c.line(img, (50,125), (200,125), (136, 252, 3), 3)   

img = c.arrowedLine(img, (55, 125), (200, 200), (252,3,219), 3)

img = c.circle(img, (200,200), 50, (86,3,252), 3)

img = c.rectangle(img, (40, 50), (210,210), (3,252,161), 5)

font = c.FONT_HERSHEY_TRIPLEX
img = c.putText(img, "Nature", (70, 90), font, 2, (128, 48,124), 3, c.LINE_AA)

c.imwrite("D:\python\Output\image_drawing2.jpg", img)

c.imshow("LandScape", img)

c.waitKey()
c.destroyAllWindows()
'''

#Drawing on VIDEO

cap= c.VideoCapture("C:\\Users\\91738\\Videos\\song.mp4")
print("Width :", cap.get(3))
print("Height :", cap.get(4))

save = c.VideoWriter_fourcc(*'XVID')
output = c.VideoWriter("d:\python\Output\draw_video_datetime.mp4", save, 20.0, (1000,700))

while (cap.isOpened):
    ret, f= cap.read()
    if ret == True:
        text = "Height :" +str(cap.get(4))+ "Width :" +str(cap.get(3))
        date = 'DATE_TIME :' +str(dt.datetime.now())
        font = c.FONT_HERSHEY_PLAIN
        f = c.putText(f, text, (20, 50), font, 3, (41, 29, 40), 3, c.LINE_AA)
        f = c.putText(f, date, (20, 100), font, 3, (41, 29, 40), 3, c.LINE_AA)
        f = c.resize(f, (1000,700))
        c.imshow("Video_Drawing", f)
        output.write(f)
        if c.waitKey(25) & 0xFF == ord("x"):
            exit(0)
cap.release()
output.release()
c.destroyAllWindows()