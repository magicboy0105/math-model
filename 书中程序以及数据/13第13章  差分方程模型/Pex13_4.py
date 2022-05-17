#程序文件Pex13_4.py
import numpy as np
from numpy.linalg import eig, inv
from matplotlib.pyplot import bar, show, legend, rc, plot
rc('font',size=16); rc('font',family='SimHei')
L=np.array([[0,4,3],[0.5,0,0],[0,0.25,0]])
X=1000*np.ones((3,1)); TX=np.zeros((3,5))
for i in range(5): X=L.dot(X); TX[:,i]=X.flatten()
print("TX=",TX)
for i in range(3): bar(np.arange(1,6)-0.25+i/4,TX[i],width=0.2)
legend(('幼龄组','二龄组','三龄组')); show()

val,vec=eig(L)  #计算特征值及对应的特征向量
cv=inv(vec).dot(1000*np.ones(3)); c=abs(cv[0])
print("特征值=",val,"\n特征向量为：\n",vec,'\nc=',c)

s=int(input("输入s的值:")); m=10  #计算10年
TY=[]; Y=np.ones(3)*1000; TY=np.zeros((m,3))
for i in range(1,m+1):
    Y=L.dot(Y)-s*np.ones(3); TY[i-1,:]=Y.flatten()
plot(np.arange(1,m+1),TY)
legend(('幼龄组','二龄组','三龄组')); show()

