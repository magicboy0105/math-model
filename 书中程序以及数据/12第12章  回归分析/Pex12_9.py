#程序文件 Pex12_9.py
import numpy as np
import statsmodels.api as sm
a=np.loadtxt("Pdata12_9.txt")
n=a.shape[1] #提取矩阵的列数
x=a[:,:n-1]; y=a[:,n-1]
md=sm.Logit(y,x)
md=md.fit(method="bfgs")  #这里必须使用bfgs方法，使用默认牛顿方法出错
print(md.params,'\n----------\n'); print(md.summary2())
print(md.predict([[-49.2,-17.2,0.3],[40.6,26.4,1.8]]))  #求预测值
