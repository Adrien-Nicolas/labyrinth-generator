import cv2
import numpy as np
import argparse
from tkinter import * 
from PIL import Image, ImageTk



img = cv2.imread('files/laby_trace.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
dc = cv2.drawContours(thresh, contours, 0, (255, 255, 255), 5)
dc = cv2.drawContours(dc, contours, 1, (0,0,0) , 5)
