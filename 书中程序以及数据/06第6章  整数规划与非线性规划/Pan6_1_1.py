#程序文件Pan6_1_1.py
import numpy as np
import pandas as pd
x0=np.array([150, 85, 150, 145, 130, 0])
y0=np.array([140, 85, 155, 50, 150, 0])
q=np.array([243, 236, 220.5, 159, 230, 52])
d=np.zeros((6,6)); a0=np.zeros((6,6)); b0=np.zeros((6,6))
xy0=np.c_[x0,y0]
for i in range(6):
    for j in range(6): d[i,j]=np.linalg.norm(xy0[i]-xy0[j])
d[np.where(d==0)]=np.inf
a0=np.arcsin(8./d)*180/np.pi
xy1=x0+1j*y0; xy2=np.exp(1j*q*np.pi/180)
for m in range(6):
    for n in range(6):
        if n!=m: b0[m,n]=np.angle((xy2[n]-xy2[m])/(xy1[m]-xy1[n]))
b0=b0*180/np.pi
f=pd.ExcelWriter('Pan6_1.xlsx')  #创建文件对象
pd.DataFrame(a0).to_excel(f,"sheet1",index=None)  #把a0写入Excel文件
pd.DataFrame(b0).to_excel(f,"sheet2",index=None)  #把b0写入表单2
f.save()

