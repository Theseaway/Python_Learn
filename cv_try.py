import cv2 as cv
import scipy as sc
import numpy as np
def get_eng(image):
    #首先定义滤波器，一般采取np.array
    fil_x=np.array(([-1,0,1],
                    [-2,0,2],
                    [-1,0,1]),dtype="float32")
    
    fil_y=np.array(([-1,-2,-1],
                    [0,0,0],
                    [1,2,1]),dtype="float32")

    fil_temp1=cv.filter2D(image,-1,fil_x)
    fil_temp2=cv.filter2D(image,-1,fil_y)
    fil_temp=fil_temp1+fil_temp2
    fil_img=np.hstack((image,fil_temp))

    cv.imshow("result",fil_img)#展示结果

    res_img=np.zeros((row,column),np.dtype('uint8'))#在调用python里面np的数组时，需要注意分配类型
    for i in range(1,row):
        for j in range(1,column):
            res_img[i][j]=fil_img[i][j+799]
    cv.imshow("energy",res_img)
    return res_img
    
def find_min(eng,dir,channels):
    #此函数用于寻找数据中最小值集合的一条曲线，这条曲线中的相邻元素为“八元素”相连的关系
    #即不能出现跳变，而只能缓慢的进行变化,当出现剧烈变化时，图像本身会发生畸变
    #为了达到这种效果，首先应该寻找一条总和最小的并且应该满足相关限制条件
    #这里的dir表示求解最小能量表是逐行还是逐列
    cv.imshow("energy",eng)
    if channels==1:#表示为灰度图
        if dir==1:#表示为从上到下
            index=np.zeros((1,row),dtype='uint8')
            j=0
            for i in range(0,row):
                if i==0:
                    minre=255
                    for j in range(1,column):
                        if minre>eng[0][j]:
                            minre=eng[0][j]
                    index[i]=j#记录最小值所在的位置
                #elif i>0:
                    #此时已有开端点，为了寻找下一个点，可以直接从此点往下寻找

    return 0

'''
    elif dir ==2:
        for i in column:
'''
    #elif channels==3:#表示为3通道图，或为HSV、HSI、RGB等
        #if 
    #return 0


img=cv.imread("test_SC.jpg")
b,g,r=cv.split(img)
#cv.imshow("Blue image",b)
#cv.imshow("Green image",g)
size=img.shape#size是一个包含3个数据的值，分别是行数、列数和通道数
row,column,channel=size
gray_img=cv.imread("test_SC.jpg",cv.IMREAD_GRAYSCALE)
#cv.namedWindow("Image")
print("原始图片的大小为",img.shape)
cv.imshow("Original_Image",img)
#cv.namedWindow("Gray_Image")
print("灰度图的大小为",gray_img.shape)
#get_eng(img)
eng_img=get_eng(gray_img)
##第一步是求得能量图，首先根据论文中最简单的公式进行求解
min_route=find_min(eng_img,1,1)

cv.imshow("Transport to gray:",gray_img)
cv.waitKey(10000)

#释放窗口
cv.destroyAllWindows() 