import cv2 as c
'''
#Border the image
i=c.imread("d:\python\capame.jpg")
while True:
    i=c.resize(i, (600,500))
    br=c.copyMakeBorder(i, 10,10,10,10,c.BORDER_CONSTANT, value = [0,0,0])
    c.imshow("Border", br)
    c.imwrite("D:\python\Output\border.jpg", br)
    if c.waitKey() & 0xFF == ord('x'):
        exit(0)

c.destroyAllWindows()
'''

# Mix the two image (blending image)
i = c.imread("d:\python\capame.jpg")
i = c.resize(i, (500,400))
c.imshow("i", i)

i1 = c.imread("d:\python\capame1.jpg")
i1 = c.resize(i1, (500,400))
c.imshow("i1", i1)

# for blending image use c.add() or c.addWweighted()
res = c.add(i,i1)
c.imshow("Blending_add", res)
c.imwrite("D:\python\Output\blending_image.jpg", res)

res_wei = c.addWeighted(i,0.5,i1,0.5,0)
c.imshow("Blending_weighted", res_wei)

c.waitKey()
c.destroyAllWindows()


