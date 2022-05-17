#程序文件Pex4_29.py
from pandas import read_excel
a=read_excel("Pdata4_29.xlsx")
b1=a.fillna(0)  #用0填补所有的缺失值
b2=a.fillna(method='ffill')  #用前一行的值填补缺失值
b3=a.fillna(method='bfill')  #用后一行的值填补，最后一行缺失值不处理
b4=a.fillna(value={'gender':a.gender.mode()[0],   #性别使用众数替换
                'age':a.age.mean(),          #年龄使用均值替换
                'income':a.income.median()}) #收入使用中位数替换
