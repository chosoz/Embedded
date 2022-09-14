import cv2
import numpy as np		
img = cv2.imread("image.jpg")
b, g, r = cv2.split(img)
merged = cv2.merge([b,g,r])  #//合并通道
print(merged.shape)      #//(240, 320, 3)   合并后顺序是(高度 宽度 通道数)
cv2.imshow("Merged", merged)
cv2.waitKey(0)	
