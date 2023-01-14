import cv2
import numpy as np
import argparse
from tkinter import * 
from PIL import Image, ImageTk


img = cv2.imread('files/laby.png')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

## get only the blue color
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])


## get only the red color
lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])


## get only the green color
lower_green = np.array([50,50,50])
upper_green = np.array([70,255,255])


mask_laby = cv2.inRange(hsv, lower_blue, upper_blue)
edges_laby = cv2.Canny(mask_laby,100,200)

#

root = Tk()
root.geometry("1800x1200")
root.title("Drawing lines to a canvas")
cv = Canvas(root,height="1800",width="1200",bg="white")
cv.pack()


"""cv2.imshow('mask_laby', mask_laby)
cv2.imshow('img', img)
cv2.imshow('edges_laby',edges_laby)
"""

edged = Image.fromarray(edges_laby)
edged = ImageTk.PhotoImage(edged)

cv.create_image(20, 20, anchor=NW, image=edged)
root.mainloop() 

cv2.waitKey(0)
cv2.destroyAllWindows()
