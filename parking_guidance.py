import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
% matplotlib inline
import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    img2 = cv2.imread('bot1.jpg')
    
    cv2.imshow('frame1',frame)

    orb = cv2.ORB()

    kp1, des1 = orb.detectAndCompute(frame, None)
    kp2, des2 = orb.detectAndCompute(img2, None)
   

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    matches = bf.match(des1,des2)

    matches = sorted(matches, key = lambda x:x.distance)

    matches = matches[:10]
    
    if matches[0]!=None:
        src_points = np.float32(map(lambda x: kp1[x.queryIdx].pt, matches[:10])).reshape(-1, 1, 2)
        dst_points = np.float32(map(lambda x: kp2[x.trainIdx].pt, matches[:10])).reshape(-1, 1, 2)
    
    
        H, _ = cv2.findHomography(src_points, dst_points)

        p1 = H.dot([1, 1, 1])
        p2 = H.dot([2, 2, 1])

        p1 = p1 / p1[-1]
        p2 = p2 / p2[-1]

        org_line_seg = np.array([2, 2]) - np.array([1, 1])
        new_line_seg = p2[:2] - p1[:2]

        angle = np.dot(org_line_seg, new_line_seg) / np.sqrt(np.sum((org_line_seg ** 2)) * np.sum(new_line_seg ** 2))

        theta = math.acos(angle)

        degree = theta*180*7/22
        print p1
   

    if cv2.waitKey(2000) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
