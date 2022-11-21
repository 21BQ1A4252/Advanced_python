import cv2 as cv
import sys
img = cv.imread(r"C:\Users\91799\OneDrive\Pictures\Saved Pictures\butterfly.png",0)
cv.imwrite(r"C:\Users\91799\OneDrive\Pictures\Saved Pictures\butterfly.png",img)
cv.imshow(r"C:\Users\91799\OneDrive\Pictures\Saved Pictures\butterfly.png",img)