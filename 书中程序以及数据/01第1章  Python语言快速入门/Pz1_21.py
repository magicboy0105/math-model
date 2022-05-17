#程序文件Pz1_21.py
import numpy as np   #导入numpy库，相当于大模块，并设置别名为np
import numpy.linalg as LA  #导入numpy库下linalg（线性代数）模块，别名为LA
a=np.linspace(0,10,5)   #产生0到10之间等间距的5个数
b=LA.norm(a)    #求b的模，即向量a的长度
print("a的长度为：%7.4f"%b)
