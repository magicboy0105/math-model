#程序文件Pex2_21.py
import numpy as np
#读前6行前8列数据
a=np.genfromtxt("Pdata2_21.txt",max_rows=6, usecols=range(8)) 
b=np.genfromtxt("Pdata2_21.txt",dtype=str,max_rows=6,usecols=[8])  #读第9列数据
b=[float(v.rstrip('kg')) for (i,v) in enumerate(b)]  #删除kg,并转换为浮点型数据
c=np.genfromtxt("Pdata2_21.txt",skip_header=6)  #读最后一行数据
print(a,'\n',b,'\n',c)
