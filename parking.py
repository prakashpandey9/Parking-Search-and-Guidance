import cv2
import math
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('new_fill.jpg')
img3 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.imread('new_parking.jpg')
img4 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

img_subtract = img3 - img4
img5 = cv2.cvtColor(img_subtract, cv2.COLOR_GRAY2RGB)

%matplotlib inline
plt.imshow(img5)

ret,thresh1 = cv2.threshold(img5,127,255,0)
titles = ['Original Image','BINARY']
images = [img5, thresh1]


for i in xrange(2):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
_, contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print contours
img7 = cv2.drawContours(thresh1, contours, -1, (255, 255, 255), 3)
for i in range(0, 11, 1):
    cnt = contours[i]
    M = cv2.moments(cnt)
    cx = int(M['m10']/M['m00'])
    print cx
    cy = int(M['m01']/M['m00'])
    print cy
    dis = math.sqrt((cx - 350)**2 + (cy - 459)**2)
    print dis
    print('  ')
    
  cx = []
cy = []
dis = []
for i in range (0, 11, 1):
    cnt = contours[i]
    M = cv2.moments(cnt)
    a = int(M['m10']/M['m00'])
    cx.append(a)
    b = int(M['m01']/M['m00'])
    cy.append(b)
    c = math.sqrt((a - 350)**2 + (b - 459)**2)
    dis.append(c)
    
print(cx)
k = (dis.index(min(dis)))
print(cx[k], cy[k])
