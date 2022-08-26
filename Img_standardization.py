import cv2 as c
from colorthief import ColorThief 
import colorsys
import matplotlib.pyplot as plt

i = c.imread("d:\python\g1.png")
ct = ColorThief("d:\python\g1.png")

# To Show Dominant Colors from Image
palette = ct.get_palette(color_count=7)
plt.imshow([[palette[i] for i in range(7)]])
plt.show()

# To get Specific color
color = int(input("Enter Index Value of White Color: "))
print("RGB value :",palette[color])
r,g,b = palette[color]
r1=255-r
g1=255-g
b1=255-b
print("Difference: (",r1,",", g1,",",b1,")")


# Conversion BGR to RGB
i1 = c.cvtColor(i, c.COLOR_BGR2RGB)

for row in range(len(i1)):
    for col in range(3):
        i1[row][col][0] += r1
        i1[row][col][1] += g1
        i1[row][col][2] += b1

i2=c.cvtColor(i1, c.COLOR_RGB2BGR)

c.imshow("Original", i)
c.imshow("Modify_Img", i2)


c.waitKey(0)
c.destroyAllWindows()




