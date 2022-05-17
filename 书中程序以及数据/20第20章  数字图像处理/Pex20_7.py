#程序文件Pex20_7.py
from PIL import Image
a=Image.new("RGB",(640,480),(50,50,100,0))  #创建新图像 
a.save("figure20_7.jpg")  #保存图像
a.show()  #显示图像
