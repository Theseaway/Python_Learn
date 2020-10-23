import cv2
import math
import numpy as np

rvec=np.array([[ 0.99007562,  2.76917734, -0.69044387]])
mtx = np.zeros((3, 3), dtype=np.float)
print(mtx)
cv2.Rodrigues(rvec,mtx,0)
print("After Rodrigues formula,we get rotation matrix like \n",mtx)
