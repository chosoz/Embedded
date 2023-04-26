//---方式一(opencv自带的函数)
import cv2
import numpy as np	
img = cv2.imread("image.jpg")  
b, g, r = cv2.split(img)  #//分离为blue,green ,red 三色通道(注：opencv 通道顺序是BGR，而不是主流的RGB)
                          #//	img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)  调整通道顺序为RGB
                          #//只分离一个 b = cv2.split(img)[0]   0:b 1:g 2:r                          
cv2.imshow("Blue", r)  
print(r.shape)            #//(240,320)
cv2.imshow("Red", g)  
cv2.imshow("Green", b)  
cv2.waitKey(0)

//---方式二(numpy的函数)
import cv2
import numpy as np	
img = cv2.imread("image.jpg")  
print(img.shape)  
r = np.zeros((img.shape[0],img.shape[1]), dtype=img.dtype)   #//创建numpy空间
r[:,:] = img[:,:,2]    #//拷贝r通道的数据
  
cv2.imshow("Red", r)  
cv2.waitKey(0) 
