#程序文件Pex4_4.py
from scipy.stats import binom
n, p=20, 0.8
mean, variance, skewness, kurtosis=binom.stats(n, p, moments='mvsk') 
#上述语句不显示，只为了说明数据顺序
print("所求的数字特征为：", binom.stats(n, p, moments='mvsk'))
