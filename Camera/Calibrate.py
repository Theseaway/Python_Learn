import cv2
import numpy as np
import glob
import matplotlib.pyplot as plt
import matplotlib.patches as patches


# 找棋盘格角点

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001) # 阈值
#棋盘格模板规格
w = 6   # 10 - 1
h = 7   # 7  - 1
# 世界坐标系中的棋盘格点,例如(0,0,0), (1,0,0), (2,0,0) ....,(8,5,0)，去掉Z坐标，记为二维矩阵
objp = np.zeros((w*h,3), np.float32)
objp[:,:2] = np.mgrid[0:w,0:h].T.reshape(-1,2)
objp = objp*29  # 18.1 mm

# 储存棋盘格角点的世界坐标和图像坐标对
objpoints = [] # 在世界坐标系中的三维点
imgpoints = [] # 在图像平面的二维点

images = glob.glob('/home/sea/图片/*.jpg')  #   拍摄的十几张棋盘图片所在目录

i = 1
for fname in images:

    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # 找到棋盘格角点
    ret, corners = cv2.findChessboardCorners(gray, (w,h),None)
    # 如果找到足够点对，将其存储起来
    if ret == True:
        print("i:", i)
        i = i+1
        cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        objpoints.append(objp)
        imgpoints.append(corners)
        # 将角点在图像上显示
        cv2.drawChessboardCorners(img, (w,h), corners, ret)
        cv2.namedWindow('findCorners', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('findCorners', 810, 405)
        cv2.imshow('findCorners',img)
        if cv2.waitKey(1000):
            cv2.destroyAllWindows()
#%% 标定
ret, mtx, dist, rvecs, tvecs = \
    cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)


print("ret:",ret  )
print("mtx:\n",mtx)      # 内参数矩阵
print("dist:\n",dist   )   # 畸变系数   distortion cofficients = (k_1,k_2,p_1,p_2,k_3)
print("rvecs:\n",rvecs)   # 旋转向量  # 外参数
print("tvecs:\n",tvecs  )  # 平移向量  # 外参数

'''
ret: 1.6690057121785065
mtx:
 [[3.15145209e+03 0.00000000e+00 1.45697200e+03]
 [0.00000000e+00 3.15703606e+03 1.99505885e+03]
 [0.00000000e+00 0.00000000e+00 1.00000000e+00]]
dist:
 [[ 0.45381735 -2.37093369 -0.00734813 -0.00426619  4.02310968]]
rvecs:
 [array([[-0.19286916],
       [-1.02316861],
       [-2.75962684]]), array([[-0.13509647],
       [ 1.09045014],
       [ 2.89261459]]), array([[0.68122357],
       [0.78626342],
       [2.76883035]])]
tvecs:
 [array([[ 64.90618583],
       [ 35.27348057],
       [252.19930634]]), array([[ 85.55528267],
       [ 50.67510568],
       [286.62648729]]), array([[ 21.54651872],
       [ 59.37457686],
       [263.80339574]])]
'''
