#程序文件Pex2_15.py
import numpy as np
a=np.array([[3,4,9],[12,15,1]])
b=np.array([[2,6,3],[7,8,12]])
print(a[a>b])  #取出a大于b的所有元素，输出：[ 3  9 12 15]
print(a[a>10]) #取出a大于10的所有元素，输出：[12 15]
print(np.where(a>10,-1,a)) #a中大于10的元素改为1
print(np.where(a>10,-1,0)) #a中大于10的元素改为1，否则为0
