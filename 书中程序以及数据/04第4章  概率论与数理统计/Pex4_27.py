#程序文件Pex4_27.py
from numpy import NaN
from pandas import Series
data=Series([10.0, None, 20, NaN, 30])
print(data.isnull())  #输出每个元素的检测结果
print("是否存在缺失值：", any(data.isnull()))  #输出：True
