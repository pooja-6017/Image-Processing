import cv2 as c
import pytesseract as pt

pt.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

i = c.imread("d:\\python\\img.jpg")
i = c.cvtColor(i, c.COLOR_BGR2RGB)

print(pt.image_to_string(i))
print(pt.image_to_boxes(i))

#Detecting Character
h,w,_ = i.shape
boxes = pt.image_to_boxes(i)
for box in boxes.splitlines():
    print(box)
    b = box.split(" ")
    print(b)
    x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    c.rectangle(i, (x,h-y), (w,h-h), (255,0,0), 2) 

c.imshow("Data_Extraction", i)
c.waitKey()
c.destroyAllWindows()