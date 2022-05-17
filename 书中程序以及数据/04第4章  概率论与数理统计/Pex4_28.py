#程序文件Pex4_28.py
from pandas import read_excel
a=read_excel("Pdata2_33.xlsx",usecols=range(1,4))
b1=a.dropna()  #删除所有的缺失值
b2=a.dropna(axis=1, thresh=9)  #删除有效数据个数小于9的列
b3=a.drop('用户B', axis=1)      #删除用户B的数据
print(b1,'\n---------------\n',b2,'\n---------------\n',b3)
