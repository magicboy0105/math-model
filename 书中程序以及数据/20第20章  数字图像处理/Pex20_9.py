#程序文件Pex20_8.py
from PIL import Image
from pylab import subplot,imshow,show
a=Image.open('flower.jpg')  #读入图像
ra,ga,ba=a.split()  #图像分割成R、G、B三个通道
c=Image.merge('RGB',(ra,ga,ba)) #三个通道合成一张彩色图像
subplot(221); imshow(ra); subplot(222); imshow(ga)
subplot(223); imshow(ba); subplot(224); imshow(c); show()
