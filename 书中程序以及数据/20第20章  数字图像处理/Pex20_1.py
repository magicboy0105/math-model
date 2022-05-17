#程序文件Pex20_1.py
import cv2
img=cv2.imread("Lena.bmp")
cv2.imshow('image',img)
cv2.imwrite('Lena.jpg',img)
