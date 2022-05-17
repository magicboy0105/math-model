#程序文件Pex19_2.py
import numpy as np
import pylab as plt
from sklearn.svm import SVR 

np.random.seed(123)
x=np.arange(200).reshape(-1,1)
y=(np.sin(x)+3+np.random.uniform(-1,1,(200,1))).ravel()

model = SVR(gamma='auto'); print(model)
model.fit(x,y); pred_y = model.predict(x)
print("原始数据与预测值前15个值对比：")
for i in range(15): print(y[i],pred_y[i])

plt.rc('font',family='SimHei'); plt.rc('font',size=15)
plt.scatter(x, y, s=5, color="blue", label="原始数据")
plt.plot(x, pred_y, '-r*',lw=1.5, label="预测值")
plt.legend(loc=1)

score=model.score(x,y); print("score:",score)
ss=((y-pred_y)**2).sum()  #计算残差平方和
print("残差平方和：", ss)
plt.show()


