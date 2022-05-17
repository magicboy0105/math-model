#程序文件Pex4_18.py
import numpy as np
from statsmodels.stats.weightstats import ttest_ind
a=np.array([0.225, 0.262, 0.217, 0.240, 0.230, 0.229, 0.235, 0.217])
b=np.array([0.209, 0.205, 0.196, 0.210, 0.202, 0.207,
            0.224, 0.223, 0.220, 0.201])
tstat, pvalue, df=ttest_ind(a, b, value=0)
print('检验统计量为：',tstat); print('p值为:',pvalue)
print('自由度为：',df)

