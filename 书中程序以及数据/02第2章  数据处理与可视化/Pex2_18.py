#程序文件Pex2_18.py
import numpy as np
a=np.arange(0,3,0.5).reshape(2,3)  #生成2×3的数组
np.savetxt("Pdata2_18_1.txt", a)  #缺省按照'%.18e'格式保存数值，以空格分隔
b=np.loadtxt("Pdata2_18_1.txt")  #返回浮点型数组
print("b=",b)
np.savetxt("Pdata2_18_2.txt", a, fmt="%d", delimiter=",")  #保存为整型数据，以逗号分隔
c=np.loadtxt("Pdata2_18_2.txt",delimiter=",")  #读入的时候也需要指定逗号分隔
print("c=",c)
