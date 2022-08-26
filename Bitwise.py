import cv2 as c
import numpy as np

i1 = np.zeros([400,400,3], np.uint8)
i2 = np.zeros([400,400,3], np.uint8)

i1 = c.rectangle(i1,(20,20), (150,150), (255,255,255), -1)
i2 = c.rectangle(i2, (60,60), (200,200), (255,255,255),-1)

#Bitwise Operation &, |, !, xor
#b_and = c.bitwise_and(i1, i2)
#b_or = c.bitwise_or(i1, i2)
#b_noti1 = c.bitwise_not(i1)
#b_noti2 = c.bitwise_not(i2)
b_xor = c.bitwise_xor(i1, i2)

#c.imshow("Bitwise_and", b_and)
#c.imshow("Bitwise_or", b_or)
#c.imshow("Bitwise_noti1", b_noti1)
#c.imshow("Bitwise_noti2", b_noti2)
c.imshow("Bitwise_xor", b_xor)
c.imshow("Image1", i1)
c.imshow("Image2", i2)

c.waitKey()
c.destroyAllWindows()