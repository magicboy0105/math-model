#程序文件Pex17_3.py
from sklearn.linear_model import Perceptron
import numpy as np
x0=np.array([[-0.5,-0.5,0.3,0.0],[-0.5,0.5,-0.5,1.0]]).T
y0=np.array([1,1,0,0])
md = Perceptron(tol=1e-3)   #构造模型
md.fit(x0, y0)              #拟合模型
print(md.coef_,md.intercept_)  #输出系数和常数项
print(md.score(x0,y0))   #模型检验
print("预测值为：",md.predict(np.array([[-0.5,0.2]])))
