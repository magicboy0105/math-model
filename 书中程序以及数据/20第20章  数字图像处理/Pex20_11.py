#程序文件Pex20_11.py
from PIL import Image
from numpy import array
a=Image.open('flower.jpg')  #读入图像
position=(100,100); b1=a.getpixel(position)  #读取像素
a.putpixel(position,tuple(array(b1)//2))  #修改像素
print(b1,a.getpixel(position))  #显示修改前后的像素值

