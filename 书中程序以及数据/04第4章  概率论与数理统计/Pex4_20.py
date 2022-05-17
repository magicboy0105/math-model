#程序文件Pex4_20.py
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
n=50; k=8 #初始小区间划分的个数
a=np.loadtxt("Pdata4_20.txt")
a=a.flatten(); mu=a.mean(); s=a.std()
print("均值为：", mu); print("标准差为：", s)
print("最大值为：",a.max()); print("最小值为：",a.min())
bins=np.array([14.2, 14.625, 14.8375, 15.05, 15.2625, 15.475, 15.9])
h=plt.hist(a,bins)
f=h[0]; x=h[1] #提取各个小区间的频数和小区间端点的取值
print("各区间的频数为：",f,"\n小区间端点值为：",x)
p=ss.norm.cdf(x, mu, s)  #计算各个分点分布函数的取值
dp=np.diff(p)  #计算各小区间取值的理论概率
dp[0]=ss.norm.cdf(x[1],mu,s)  #修改第一个区间的概率值
dp[-1]=1-ss.norm.cdf(x[-2],mu,s)  #修改最后一个区间的概率值
print("各小区取值的理论概率为：",dp)
st=sum(f**2/(n*dp))-n  #计算卡方统计量的值
bd=ss.chi2.ppf(0.95,k-5) #计算上alpha分位数
print("统计量为：{}，临界值为：{}".format(st,bd))
