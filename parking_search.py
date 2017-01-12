import cv2 as cv
import math
import numpy as np
from matplotlib import pyplot as plt

img1 = cv.imread('C:\Users\Sunny Singh\Pictures\parkingfull.jpg')
img3 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)

img2 = cv.imread('C:\Users\Sunny Singh\Pictures\parkingfill.jpg')
img4 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

img_subtract = img3 - img4
img5 = cv.cvtColor(img_subtract, cv.COLOR_GRAY2BGR)

kernel = np.ones((5,5),np.uint8)
img8 = cv.erode(img5, kernel, iterations =5)
#%matplotlib inline
#plt.imshow(img8)

ret, thresh1 = cv.threshold(img8, 127, 255, 0)
titles = ['Original Image', 'BINARY']
images = [img8, thresh1]
img6 = cv.cvtColor(thresh1, cv.COLOR_BGR2GRAY)

#for i in xrange(2):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
	
contours, hierarchy = cv.findContours(img6,cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#print contours

#img7 = cv.drawContours(img6, contours, -1, (255,255,255), 3)
#print img7
#print len(contours)

if len(contours)>0:
    for i in range(0,len(contours),1):
        cnt= contours[i]
        M = cv.moments(cnt)
        cx = int(M['m10']/M['m00'])
        print cx
        cy = int(M['m01']/M['m00'])
        print cy
        dis = math.sqrt((cx - 350)**2 + (cy - 459)**2)
        print dis
        print('  ')
else:
    print "sorry no lot is empty"