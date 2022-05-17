#程序文件Pex4_25_3.py
import statsmodels.api as sm
import numpy as np
x=np.array([2.5, 3.9, 2.9, 2.4, 2.9, 0.8, 9.1, 0.8, 0.7,
    7.9, 1.8, 1.9, 0.8, 6.5, 1.6, 5.8, 1.3, 1.2, 2.7])
y=np.array([211, 167, 131, 191, 220, 297, 71, 211, 300,
    107, 167, 266, 277, 86, 207, 115, 285, 199, 172])
X=sm.add_constant(x)
md=sm.OLS(y,X).fit()  #构建并拟合模型
print(md.params,'\n--------\n')  #提取回归系数
print(md.summary2())
ypred=md.predict([1,8])  #第一列必须加1
print("预测值为：",ypred)
