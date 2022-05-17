#程序文件Pex12_10.py
import numpy as np
from sklearn.linear_model import LogisticRegression
a=np.loadtxt("Pdata12_9.txt")
n=a.shape[1]  #提取矩阵的列数
x=a[:,:n-1]; y=a[:,n-1]
md=LogisticRegression(solver='lbfgs')
md=md.fit(x,y)
print(md.intercept_,md.coef_)
print(md.predict(x))   #检验预测模型
print(md.predict([[-49.2,-17.2,0.3],[40.6,26.4,1.8]]))  #求预测值
