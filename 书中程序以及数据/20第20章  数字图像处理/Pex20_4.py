#程序文件Pex20_4.py
from PIL import Image
from numpy import array
import pylab as plt  #加载Matplotlib的Pylab接口
a=Image.open("empire.jpg")  #返回一个PIL图像对象
b=a.convert("L")  #转换为灰度图像对象
b.save("empire2.jpg")  #把灰度图像保存到empire2.jpg
aa=array(a)  #把图像对象转换为数组
print(aa.shape)  #显示图像的大小
#左上角为坐标原点，下面裁剪左上右下指定区域
c=a.crop((100,100,400,400)) 
d=a.rotate(45)  #图像旋转45度
plt.rc('font',family="SimHei")
plt.subplot(221); plt.imshow(a); plt.title("原图")
plt.subplot(222); plt.imshow(b); plt.title("灰度图")
plt.subplot(223); plt.imshow(c); plt.title("剪裁图像")
plt.subplot(224); plt.imshow(d); plt.title("旋转图像"); plt.show()
