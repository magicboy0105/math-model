#程序文件Pex20_12.py
from PIL import Image,ImageDraw
from numpy import array
a=Image.open('flower.jpg')  #读入图像
w,h=a.size  #读入图像的宽度和高度
b=ImageDraw.Draw(a)  #实例化Draw类
b.line(((0,0),(w-1,h-1)),fill=(255,0,0))
b.line(((w-1,0),(0,h-1)),fill=(255,0,0))
b.arc((0,0,w-1,h-1),0,360,fill=(255,0,0))
a.show(); a.save("figure20_12.png")  #显示并保存图像
