#程序文件Pex12_3.py
import numpy as np; import statsmodels.api as sm
a=np.loadtxt("Pdata12_3.txt")   #加载表中x1,x2,x3,y的11行4列数据
x=a[:,:3]  #提出自变量观测值矩阵
X=sm.add_constant(x)  #增加第一列全部元素为1得到增广矩阵
md=sm.OLS(a[:,3],X).fit()  #构建并拟合模型
b=md.params          #提取所有回归系数
y=md.predict(X)      #求已知自变量值的预测值
print(md.summary())  #输出模型的所有结果
print("相关系数矩阵:\n",np.corrcoef(x.T))
X1=sm.add_constant(a[:,0])
md1=sm.OLS(a[:,2],X1).fit()
print("回归系数为：",md1.params)
