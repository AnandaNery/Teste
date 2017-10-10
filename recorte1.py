import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r'C:\Users\Ananda\Desktop\visao_computacional\transf_de_hough\12-56_cam_1_image_1.tif',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
output = cimg.copy()

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT, 1.5, 1700)


circles = np.uint16(np.around(circles))
for (x, y, r) in circles[0,:]:

    # draw the outer circle
    cv2.circle(output,(x, y), int(2*r),(0,255,0),3)
    # draw the center of the circle
    cv2.circle(output,(x,y),2,(0,0,255),4)
    

r1=2*r
recorte=output[y-r1:y+r1,x-r1:x+r1]
plt.imshow(recorte)
plt.show()
cv2.waitKey(0)

