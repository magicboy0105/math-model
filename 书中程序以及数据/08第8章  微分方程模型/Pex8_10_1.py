#程序文件Pex8_10_1.py
import numpy as np
from scipy.optimize import curve_fit
a=[]; b=[];
with open("Pdata8_10_1.txt") as f:    #打开文件并绑定对象f
    s=f.read().splitlines()  #返回每一行的数据
for i in range(0, len(s),2):  #读入奇数行数据
    d1=s[i].split("\t")
    for j in range(len(d1)):
        if d1[j]!="": a.append(eval(d1[j]))  #把非空的字符串转换为年代数据
for i in range(1, len(s), 2):  #读入偶数行数据
    d2=s[i].split("\t")
    for j in range(len(d2)):
        if d2[j] != "": b.append(eval(d2[j])) #把非空的字符串转换为人口数据
c=np.vstack((a,b))  #构造两行的数组
np.savetxt("Pdata8_10_2.txt", c)  #把数据保存起来供下面使用
x=lambda t, r, xm: xm/(1+(xm/3.9-1)*np.exp(-r*(t-1790)))
bd=((0, 200), (0.1,1000))  #约束两个参数的下界和上界
popt, pcov=curve_fit(x, a[1:], b[1:], bounds=bd)
print(popt); print("2010年的预测值为：", x(2010, *popt))

