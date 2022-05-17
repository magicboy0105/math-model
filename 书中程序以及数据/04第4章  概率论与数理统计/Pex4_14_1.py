#程序文件Pex4_14_1.py
from numpy import array, sqrt
from scipy.stats import t
a=array([506,  508,  499,  503,  504,  510,  497,  512,
514,  505,  493,  496,  506,  502,  509,  496])
# ddof取值为1时，标准偏差除的是(N-1)；NumPy中的std计算默认是除以N
mu=a.mean(); s=a.std(ddof=1)  #计算均值和标准差
print(mu, s); alpha=0.05; n=len(a)
val=(mu-s/sqrt(n)*t.ppf(1-alpha/2,n-1),mu+s/sqrt(n)*t.ppf(1-alpha/2,n-1))
print("置信区间为：",val)
