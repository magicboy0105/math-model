#程序文件Pex20_13.py
from PIL import Image,ImageDraw, ImageFont
a=Image.open('flower.jpg')  #读入图像
b=ImageDraw.Draw(a) #实例化Draw类
myfont=ImageFont.truetype("c:\\Windows\\Fonts\\simsun.ttc",48)
b.text((20,20),"美丽的花",font=myfont,fill=(255,0,0))
a.show(); a.save("figure20_13.png")
