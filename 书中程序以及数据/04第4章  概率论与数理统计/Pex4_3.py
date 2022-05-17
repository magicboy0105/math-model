#程序文件Pex4_3.py
from scipy.stats import binom
n, p=20, 0.8
print("期望和方差分布为：", binom.stats(n,p))
