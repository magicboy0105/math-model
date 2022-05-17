#程序文件Pex12_7.py
import numpy as np
import statsmodels.api as sm
a=np.loadtxt("Pdata12_7_1.txt")   #加载表中x,ni,mi的9行3列数据
x=a[:,0]; pi=a[:,2]/a[:,1]
X=sm.add_constant(x); yi=np.log(pi/(1-pi))
md=sm.OLS(yi,X).fit()  #构建并拟合模型
print(md.summary())  #输出模型的所有结果
b=md.params  #提出所有的回归系数
p0=1/(1+np.exp(-np.dot(b,[1,9])))
print("所求概率p0=%.4f"%p0)
np.savetxt("Pdata12_7_2.txt", b)  #把回归系数保存到文本文件
