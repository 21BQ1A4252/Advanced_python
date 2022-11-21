import cv2 as cv
import matplotlib.pyplot as pp
import sys
img = cv.imread(r"C:\Users\91799\OneDrive\Pictures\Saved Pictures\butterfly.png",1)
if img is None:
 sys.exit("Could not read the image.")
cv.imshow(r"Image",img)