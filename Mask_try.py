import cv2 
import numpy as np
img1=cv2.imread('test_SC.jpg')
img2=cv2.imread('cv2Logo.png')

##
# 
# 预处理
rows,cols,channels=img2.shape#读出添加图片的大小便于后续进行add操作
# roi=img1[img1.shape[0]-rows:img1.shape[0],img1.shape[1]-cols:img1.shape[1]]
roi=img1[0:rows,0:cols]
#当roi的选择不同时，最终得到的结果也不同
img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow("grayimage",img2gray)#没有经过处理的灰度图

## 
# 
# 创建mask和inverse_mask
ret,mask=cv2.threshold(img2gray,175,255,cv2.THRESH_BINARY)
cv2.imshow("mask",mask)#通过设计一个阈值

mask_inv=cv2.bitwise_not(mask)
cv2.imshow("inverse mask",mask_inv)
#mask用于原始图像
img1_bg=cv2.bitwise_and(roi,roi,mask=mask)
cv2.imshow("img1_bg",img1_bg)
#inverse_mask用于待添加的图像
img2_bg=cv2.bitwise_and(img2,img2,mask=mask_inv)
cv2.imshow("img2_bg",img2_bg)

## 图像加法
dst=cv2.add(img1_bg,img2_bg)
img1[0:rows,0:cols]=dst
cv2.imshow("result",img1)
cv2.waitKey(29999)
cv2.destroyAllWindows()