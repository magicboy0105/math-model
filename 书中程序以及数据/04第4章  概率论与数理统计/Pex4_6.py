#程序文件Pex4_6.py
from numpy import reshape, hstack, mean, median, ptp, var, std, cov, corrcoef
import pandas as pd
df = pd.read_excel("Pdata4_6_1.xlsx",header=None)
a=df.values  #提取数据矩阵
h=a[:,::2]  #提取奇数列身高
w=a[:,1::2]  #提取偶数列体重
h=reshape(h,(-1, 1)) #转换成列向量，自动计算行数
w=reshape(w,(-1, 1)) #转换成列向量，自动计算行数
hw=hstack([h,w])  #构造两列的数组
print([mean(h),median(h),ptp(h),var(h),std(h)])  #计算均值,中位数,极差,方差,标准差
print("协方差为：{}\n相关系数为：{}".format(cov(hw.T)[0,1],corrcoef(hw.T)[0,1]))
