import numpy as np
import cv2 as c

i = c.imread("D:\python\g1.png")
i1 = c.cvtColor(i, c.COLOR_BGR2RGB)

for row in range(len(i1)):
    for col in range(3):
        i1[row][col][0] += 41
        i1[row][col][1] += 47
        i1[row][col][2] += 85
        
i2=c.cvtColor(i1, c.COLOR_RGB2BGR)

c.imshow("Original", i)
c.imshow("Modify_Img", i2)

#save
c.imwrite("D:\python\Output\Modified_img1.jpg", i2)

c.waitKey()
c.destroyAllWindows()


#to find dominant color from image using k means cluster algorithm
# import cv2
# import numpy as np

# def create_bar(height, width, color):
#     bar = np.zeros((height, width, 3), np.uint8)
#     bar[:] = color
#     red, green, blue = int(color[2]), int(color[1]), int(color[0])
#     return bar, (red, green, blue)

# img = cv2.imread('D:\python\g1.png')
# height, width, _ = np.shape(img)
# # print(height, width)

# data = np.reshape(img, (height * width, 3))
# data = np.float32(data)

# number_clusters = 5
# criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# flags = cv2.KMEANS_RANDOM_CENTERS
# compactness, labels, centers = cv2.kmeans(data, number_clusters, None, criteria, 10, flags)
# # print(centers)

# font = cv2.FONT_HERSHEY_SIMPLEX
# bars = []
# rgb_values = []

# for index, row in enumerate(centers):
#     bar, rgb = create_bar(200, 200, row)
#     bars.append(bar)
#     rgb_values.append(rgb)

# img_bar = np.hstack(bars)

# for i, row in enumerate(rgb_values):
#     print(i)
#     image = cv2.putText(img_bar, f'RGB: {row}', (200*i,100), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)

# cv2.imshow('Image', img)
# cv2.imshow('Dominant colors', img_bar)

# cv2.waitKey(0)