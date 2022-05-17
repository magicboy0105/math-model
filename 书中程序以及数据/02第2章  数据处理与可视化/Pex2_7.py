#程序文件Pex2_7.py
from numpy import array, nan, isnan
a=array([[1, nan, 2], [4, nan, 3]])
b=a[~isnan(a)]  #提取a中非nan的数
print("b=",b)
print("b中大于2的元素有：", b[b>2])



