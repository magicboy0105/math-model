#程序文件Pex2_4.py
import numpy as np
a=np.random.randint(1,11,(3,5))  #生成[1,11 )区间上3行5列的随机整数数组
print("维数：",a.ndim);   #维数：2
print("维度：",a.shape)       #维度：（3,5）
print("元素总数：",a.size);    #元素总数：15
print("类型：",a.dtype)       #类型：int32
print("每个元素字节数：",a.itemsize)  #字节数：4
