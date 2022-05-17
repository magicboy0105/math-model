#程序文件Pex4_17.py
import numpy as np
from statsmodels.stats.weightstats import ztest
a=np.array([16, 25, 21, 20, 23, 21, 19, 15, 13,
            23, 17, 20, 29, 18, 22, 16, 22])
tstat, pvalue=ztest(a,value=21, alternative='smaller')
print('检验统计量为：',tstat); print('p值为:',pvalue)

