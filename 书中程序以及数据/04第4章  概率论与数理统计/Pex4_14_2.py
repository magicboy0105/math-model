#程序文件Pex4_14_2.py
import numpy as np
import scipy.stats as ss
from scipy import stats
a=np.array([506,  508,  499,  503,  504,  510,  497,  512,
514,  505,  493,  496,  506,  502,  509,  496])
alpha=0.95; df=len(a)-1
ci=ss.t.interval(alpha,df,loc=a.mean(),scale=ss.sem(a))
print("置信区间为：",ci)
