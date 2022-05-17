#程序文件Pex20_5.py
from PIL import Image
from numpy import array
import pylab as plt  #加载Matplotlib的Pylab接口
#下面读取图像到数组中
a=array(Image.open("empire.jpg").convert('L'))
plt.rc('font',size=16)
plt.subplot(121); plt.contour(a,origin='image')  #轮廓图
plt.subplot(122); plt.hist(a.flatten(),128); plt.show()
