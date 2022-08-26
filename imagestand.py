import numpy as np
import cv2 as c
import time as t
import random as r

i = c.imread("D:\python\g1.png")
i1 = c.cvtColor(i, c.COLOR_BGR2RGB)

print(i1)

for row in range(len(i1)):
    for col in range(3):
        i1[row][col][0] += 38
        i1[row][col][1] += 45
        i1[row][col][2] += 50
        


print("#################3")
print(i1)
i2=c.cvtColor(i1, c.COLOR_RGB2BGR)
c.imshow("Original Grapes", i)

c.imwrite("D:\python\Output\converted.jpg", i2)
c.imshow("convert Grapes", i2)


'''##  Add New single color pixel in a image blue red green white and black
print(i[0][0])
i_copy = i.copy()

# i_copy[0][0] = np.array([255, 255, 255])
# i_copy[0][1] = np.array([0, 0, 0])
# i_copy[0][2] = np.array([0, 0, 255])
# i_copy[0][3] = np.array([0, 255, 0])
# i_copy[0][4] = np.array([255, 0, 0])'''

# ## add new color pixel in a row of image
# h, w, _ = i.shape
# print(h, w)
# '''
# for c_i in range(w):
#     i_copy[0][c_i] = np.array([255,255,255])
#     i_copy[1][c_i] = np.array([0, 0, 0])
#     i_copy[2][c_i] = np.array([0, 0, 255])
#     i_copy[3][c_i] = np.array([0, 255, 0])
#     i_copy[4][c_i] = np.array([255, 0, 0])

# ## add a new color pixel in a row of an image with logic
# for r_i in range(h):
#     if r_i % 2 == 0:
#             for c_i in range(w):
#                 if c_i % 2 == 0:
#                     white_px = r.randint(0, 255)
#                     white_px1 = r.randint(0, 255)
#                     white_px2 = r.randint(0, 255)
#                     #rand_col = r.randint(0, w-1)
#                     i_copy[r_i][c_i] = np.array([255, 255, 255])'''

# ## add a new color pixel in image
# for  r_i in range(h):
#     for c_i in range(w):
#         i_copy[r_i][c_i] = np.array([])
            


#c.imshow("AfterModification", i_copy)'''
c.waitKey()
c.destroyAllWindows()