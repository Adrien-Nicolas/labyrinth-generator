import cv2
import numpy as np
from tkinter import * 
from PIL import Image, ImageTk


img = cv2.imread('files/top_left.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

## get only the blue color
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])


# get only black color
lower_black = np.array([0,0,0])
upper_black = np.array([180,255,30])



#get only the red color
lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])

#get onlu the green color
lower_green = np.array([50,50,50])
upper_green = np.array([70,255,255])




# show mask
mask_laby = cv2.inRange(hsv, lower_black, upper_black)
cv2.imshow('mask_laby', mask_laby)

#show contour of img
edges_laby = cv2.Canny(mask_laby,100,200)
edges = cv2.imshow('edges_laby',edges_laby)



#get coords of canny detection
contours, hierarchy = cv2.findContours(edges_laby, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    print(x,y,w,h)

cv2.imshow('img',img)


#export img
cv2.imwrite('files/img1_out.png',img)


cv2.waitKey(0)
cv2.destroyAllWindows()


