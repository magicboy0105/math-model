#程序文件Pex4_30.py
from pandas import read_excel
import numpy as np
a=read_excel("Pdata4_29.xlsx")
b=a.fillna(value={'gender':a.gender.mode()[0],   #性别使用众数替换
                   'age':a.age.interpolate(method='polynomial', order=2),
#年龄使用二次多项式插值替换
                   'income':a.income.interpolate()}) #收入使用线性插值替换

