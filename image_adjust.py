import cv2
import numpy as np
# while 1:
#     img1=cv2.imread("qipan.png")
#     print(img1.shape)
#     cv2.imshow("qipan1",img1)
#
#     img2=img1[0:359,0:629]
#     cv2.imshow("qipan2",img2)
#     k=cv2.waitKey(30) & 0xff
#     if k==27:
#         break
img2=cv2.imread("qipan_now.png")
cv2.imshow("qipan2",img2)
# cv2.imwrite("qipan_now.png",img2)
img3=np.arange(720*630*3).reshape(720,630,3)
# img3=np.zeros_like(y,dtype='uint8')
img3[0:360,0:630]=img2.copy()
img3[360:720,0:630]=img2.copy()
# cv2.imshow("qipan3",img3)
print(img3.shape())
cv2.imwrite("qipan_now1.png",img3)

k=cv2.waitKey(30) & 0xff
if cv2.waitKey():
    cv2.destroyAllWindows()