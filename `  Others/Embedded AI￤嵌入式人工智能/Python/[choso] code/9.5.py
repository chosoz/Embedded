from PIL import Image

img=Image.open('./image.jpg')
print(img.format,img.size,img.mode)
# img=img.convert('L')
img=img.transpose(Image.FLIP_LEFT_RIGHT)
print(img.format,img.size,img.mode)
img.show()
# img=Image.open('./image.jpg')
# img.show()

print(img.format)


