#程序文件Pex4_7.py
from numpy import reshape, c_
import pandas as pd
df = pd.read_excel("Pdata4_6_1.xlsx",header=None)
a=df.values; h1=a[:,::2]; w1=a[:,1::2]
h2=reshape(h1,(-1, 1)); w2=reshape(w1,(-1, 1))
df2=pd.DataFrame(c_[h2,w2],columns=["身高","体重"])  #构造数据框
print("求得的描述统计量如下：\n",df2.describe())
print("偏度为：\n",df2.skew())
print("峰度为：\n",df2.kurt())
print("分位数为：\n",df2.quantile(0.9))
