#程序文件Pex4_16.py
import numpy as np
from statsmodels.stats.weightstats import ztest
a=np.array([3.25, 3.27, 3.24, 3.26, 3.24])
tstat, pvalue=ztest(a,value=3.25)
print('检验统计量为：',tstat); print('p值为:',pvalue)

