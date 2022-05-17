#程序文件Pex20_14.py
from PIL import Image,ImageFilter
from pylab import subplot, show, imshow
a=Image.open('flower.jpg')  #读入图像
b=a.filter(ImageFilter.CONTOUR)  #使用轮廓滤镜
subplot(121); imshow(a)
subplot(122); imshow(b); show()
