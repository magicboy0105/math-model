 #程序文件Pex12_6.py
import numpy as np; import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.linear_model import Lasso
from scipy.stats import zscore
#plt.rc('text', usetex=True)  #没装LaTeX宏包把该句注释
a=np.loadtxt("Pdata12_6.txt")  #加载表中的9行5列数据
n=a.shape[1]-1  #自变量的总个数
x=a[:,:n]  #提出自变量观测值矩阵
X = sm.add_constant(x)
md=sm.OLS(a[:,n],X).fit()  #构建并拟合模型
print(md.summary())  #输出模型的所有结果

aa=zscore(a)  #数据标准化
x=aa[:,:n]; y=aa[:,n]  #提出自变量和因变量观测值矩阵
b=[]  #用于存储回归系数的空列表
kk=np.logspace(-4,0,100)  #循环迭代的不同k值
for k in kk:
    md=Lasso(alpha=k).fit(x,y)
    b.append(md.coef_)
st=['s-r','*-k','p-b','^-y']  #下面画图的控制字符串
for i in range(n): plt.plot(kk,np.array(b)[:,i],st[i]);
plt.legend(['$x_1$','$x_2$','$x_3$','$x_4$'],fontsize=15); plt.show()
md0=Lasso(0.05).fit(x,y)  #构建并拟合模型
cs0=md0.coef_  #提出标准化数据的回归系数b1,b2,b3,b4
print("标准化数据的所有回归系数为：",cs0)
mu=a.mean(axis=0); s=a.std(axis=0,ddof=1) #计算所有指标的均值和标准差
params=[mu[-1]-s[-1]*sum(cs0*mu[:-1]/s[:-1]),s[-1]*cs0/s[:-1]] 
print("原数据的回归系数为：",params)
print("拟合优度：",md0.score(x,y))
