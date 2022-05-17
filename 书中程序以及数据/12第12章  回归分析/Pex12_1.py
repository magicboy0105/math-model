#程序文件Pex12_1.py
import numpy as np
from sklearn.linear_model import LinearRegression
a=np.loadtxt("Pdata12_1.txt")   #加载表中x1,x2,y的13行3列数据
md=LinearRegression().fit(a[:,:2],a[:,2])    #构建并拟合模型
y=md.predict(a[:,:2])       #求预测值
b0=md.intercept_; b12=md.coef_   #输出回归系数
R2=md.score(a[:,:2],a[:,2])      #计算R^2
print("b0=%.4f\nb12=%.4f%10.4f"%(b0,b12[0],b12[1]))
print("拟合优度R^2=%.4f"%R2)
