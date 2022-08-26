import cv2 as cv
i = cv.imread("D:\\python\\nature.jpg")
print(i)
cv.imshow("Nature", i)
i = cv.resize(i,(560,400))
cv.waitKey()
cv.destroyAllWindows()
