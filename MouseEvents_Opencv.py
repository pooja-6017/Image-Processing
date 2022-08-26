import cv2 as c
import numpy as np
'''
def draw(event, x, y, flag, pm):
    print("Event :", event)
    print("X :",x)
    print("Y :", y)
    print("Flags :", flag)
    print("Parameter :" ,pm)
    if event == c.EVENT_LBUTTONDBLCLK:
        c.circle(i, (x, y), 50, (122, 48, 179),-2)
    if event == c.EVENT_RBUTTONDBLCLK:
        c.rectangle(i, (x ,y), (x+50, y+50), (24, 222, 202),5)

c.namedWindow(winname = "MOUSE EVENT")
i = np.zeros([500,500,3], np.uint8)
c.setMouseCallback("MOUSE EVENT", draw)

while True:
    c.imshow("MOUSE EVENT", i)
    c.imwrite("d:\python\Output\Mouse_event.png", i)
    if c.waitKey(1) & 0xFF == ord("x"):
        exit(0)
c.distroyAllWindow()
'''
def draw(e, x, y, f, p):
    f = c.FONT_HERSHEY_PLAIN
    if e==c.EVENT_LBUTTONDOWN:
        print(x, ', ',y)
        cord = str(x)+ ', '+str(y)
        c.putText(i, cord, (x, y), f, 1, (255,255,255),2)
        #c.imshow("findxy_color", i)
    if e==c.EVENT_RBUTTONDOWN:
        b=i[y,x,0]
        g=i[y,x,1]
        r=i[y,x,2]

        color = str(b)+ ', ' +str(g)+ ", "+str(r)
        c.putText(i, color, (x, y), f, 1, (255,255,255), 2)
        #c.imshow("findxy_color", i) 

c.namedWindow(winname="FIND_X_Y_COLOR")
i= c.imread("d:\python\img1.webp")
c.setMouseCallback("FIND_X_Y_COLOR", draw)
while True:
    i = c.resize(i, (800, 700))
    c.imshow("FIND_X_Y_COLOR", i)
    c.imwrite("d:\python\Output\FIND_X_Y_COLOR.png", i)
    if c.waitKey(1) & 0xFF == ord('x'):       #Esc
          exit(0)
c.destroyAllWindow()
