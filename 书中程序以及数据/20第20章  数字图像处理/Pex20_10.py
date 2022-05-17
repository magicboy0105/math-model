#程序文件Pex20_10.py
from PIL import Image
a=Image.open('flower.jpg')  #读入图像
b=Image.open('logo.jpg')
print(a.size,b.size)  #显示图像的大小
c=b.resize((50,50))  #把图像缩小
a.paste(c,(20,20)); a.show()  #粘贴图像并显示
