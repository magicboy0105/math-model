#程序文件Pex4_31.py
from pandas import read_csv
import numpy as np
import matplotlib.pyplot as plt
a=read_csv("sunspots.csv")
mu=a.counts.mean()  #计算黑子个数年平均值
s=a.counts.std()  #计算黑子个数标准差
print("标准差法异常值上限检测：",any(a.counts>mu+2*s))  #输出：True
print("标准差法异常值下限检测：",any(a.counts<mu-2*s))  #输出：False
Q1=a.counts.quantile(0.25)  #计算下四分位数
Q3=a.counts.quantile(0.75)  #计算上四分位数
IQR=Q3-Q1
print("箱线图法异常值上限检测：",any(a.counts>Q3+1.5*IQR))  #输出：True
print("箱线图法异常值下限检测：",any(a.counts<Q1-1.5*IQR))  #输出：False
plt.style.use('ggplot')  #设置绘图风格
a.counts.plot(kind='hist',bins=30,density=True)  #绘制直方图
a.counts.plot(kind='kde')  #绘制核密度曲线
plt.show()
print("异常值替换前的数据统计特征",a.counts.describe())
UB=Q3+1.5*IQR;
st=a.counts[a.counts<UB].max()  #找出低于判别上限的最大值
print("判别异常值的上限临界值为:",UB)
print("用以替换异常值的数据为：",st)
a.loc[a.counts>UB, 'counts']=st  #替换超过判别上限异常值
print("异常值替换后的数据统计特征",a.counts.describe())
