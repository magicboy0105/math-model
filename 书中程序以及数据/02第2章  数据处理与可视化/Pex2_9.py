#程序文件Pex2_9.py
import numpy as np
x = np.array([[1,2],[3,4],[5,6]])
x[2,0] = -1  #修改第3行、第1列元素为-1
y=np.delete(x,2,axis=0)   #删除数组的第3行
z=np.delete(y,0, axis=1)  #删除数组的第1列
t1=np.append(x,[[7,8]],axis=0) #增加一行
t2=np.append(x,[[9],[10],[11]],axis=1) #增加一列
