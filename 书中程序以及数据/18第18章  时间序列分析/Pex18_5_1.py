#程序文件Pex18_5_1.py
import pandas as pd, numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
plt.rc('font',family='SimHei'); plt.rc('font',size=16)
d=pd.read_csv('sunspots.csv',usecols=['counts'])
md=sm.tsa.ARMA(d,(9,1)).fit()
years=np.arange(1700,1989)  #已知观测值的年代
dhat=md.predict()
plt.plot(years[-20:],d.values[-20:],'o-k')
plt.plot(years[-20:],dhat.values[-20:],'P--')
plt.legend(('原始观测值','预测值')); plt.show()
dnext=md.predict(d.shape[0],d.shape[0])
print(dnext)  #显示下一期的预测值






