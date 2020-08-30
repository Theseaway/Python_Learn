from tqdm import trange
from imageio import imread, imwrite
from scipy.ndimage.filters import convolve
import sys
import numpy as np
def get_eng(image):
    #首先定义滤波器，一般采取np.array
    fil_x=np.array(([-1,0,1],
                    [-2,0,2],
                    [-1,0,1]))
    
    fil_x = np.stack([fil_x] * 3, axis=2)
    
    fil_y=np.array(([-1,-2,-1],
                    [0,0,0],
                    [1,2,1]))
    fil_y = np.stack([fil_y] * 3, axis=2)
    image=image.astype("float32")
    fil_temp=np.absolute(convolve(image,fil_x))+np.absolute(convolve(image,fil_y))
    energy=fil_temp.sum(axis=2)
    
    return energy
    
def find_min(eng,row,column):
    #此函数用于寻找数据中最小值集合的一条曲线，这条曲线中的相邻元素为“八元素”相连的关系
    #即不能出现跳变，而只能缓慢的进行变化,当出现剧烈变化时，图像本身会发生畸变
    #为了达到这种效果，首先应该寻找一条总和最小的并且应该满足相关限制条件
    #这里的dir表示求解最小能量表是逐行还是逐列
    route=np.zeros_like(eng,dtype=np.int)
    for i in range(1,row):
        for j in range(0,column):
            if j==0:
                temp=np.argmin(eng[i-1,j:j+2])
                route[i,j]=temp+j
            elif j>0:
                temp=np.argmin(eng[i-1,j-1:j+2])
                route[i,j]=temp+j-1
                    #此已有开端点，为了寻找下一个点，可以直接从此点往下寻找
    return route


img=imread("test_SC.jpg")
size=img.shape#size是一个包含3个数据的值，分别是行数、列数和通道数
row,column,channel=size

gray_img=imread("test_SC.jpg")
print("原始图片的大小为",img.shape)
imwrite("Original_Image.jpg",img)
print("灰度图的大小为",gray_img.shape)

eng_img=get_eng(img)
imwrite("./energy image.jpg",eng_img)

start=390
route=find_min(eng_img,row,column)

for i in range(1,row):
    for j in range(1,column):
        eng_img
imwrite("Route in Image.jpg",gray_img)
