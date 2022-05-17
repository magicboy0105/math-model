#程序文件Pex20_8.py
from PIL import Image
from pylab import subplot,imshow,show
a=Image.open('flower.jpg')  #读入图像
b=a.resize((128,128))  #改变图像尺寸
c=b.convert('CMYK')  #转换为CMYK模式
subplot(121); imshow(b)
subplot(122); imshow(c); show()

