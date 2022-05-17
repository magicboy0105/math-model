#程序文件Pex4_14_3.py
import numpy as np
from statsmodels.stats.weightstats import zconfint
from scipy import stats
a=np.array([506,  508,  499,  503,  504,  510,  497,  512,
514,  505,  493,  496,  506,  502,  509,  496])
ci=zconfint(a)
print("置信区间为：",ci)
