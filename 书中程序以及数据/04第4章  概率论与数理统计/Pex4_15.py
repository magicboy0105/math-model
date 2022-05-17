#程序文件Pex4_15.py
import numpy as np
from statsmodels.stats.weightstats import ztest
sigma=0.015
a=np.array([0.497, 0.506, 0.518, 0.524, 0.498, 0.511, 0.520, 0.515, 0.512])
tstat1, pvalue=ztest(a,value=0.5)  #计算T统计量的观测值及p值
tstat2=tstat1*a.std(ddof=1)/sigma  #转换为Z统计量的观测值
print('t值为：',round(tstat1,4))
print('z值为：',round(tstat2,4)); print('p值为:',round(pvalue,4))
