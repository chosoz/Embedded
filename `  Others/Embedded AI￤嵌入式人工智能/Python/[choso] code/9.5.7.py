import numpy as np
from PIL import Image
img = Image.open('image.jpg') 
img = img.convert('L') #//转为灰度图像(1像素 占8位)
obj= np.array(img)  #//图像转为numpy
print(obj.shape)    #//(28 28)  图像矩阵形状为 28行 *28列

#//输出图像数据 -> 8字 的像素矩阵
for i in range(obj.shape[0]):
  for j in range(obj.shape[1]):
    print('{0:3d} '.format(obj[i][j]),end="")  #//i:图像行号 j:图像列号   
  print('')

print('image.jpg')

print('image.jpg')








