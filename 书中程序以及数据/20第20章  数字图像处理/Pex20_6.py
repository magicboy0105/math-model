#程序文件Pex20_6.py
from PIL import Image
a=Image.open('flower.jpg')  #读入图像
a.show()  #显示图片
print(a.mode, a.size, a.format) #显示图片信息
a.save("flower2.png")  #另存为另一文件
