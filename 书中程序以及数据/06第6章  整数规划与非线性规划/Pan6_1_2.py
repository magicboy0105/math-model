#程序文件Pan6_1_2.py
import numpy as np
import pandas as pd
from scipy.optimize import minimize
a0=pd.read_excel("Pan6_1.xlsx")    #读入第1个表单
b0=pd.read_excel("Pan6_1.xlsx",1)  #读入第2个表单
a0=a0.values; b0=b0.values  #提取数值
obj=lambda x: np.sum(np.abs(x))
bd=[(-30,30) for i in range(6)]   #决策向量的界限
x0=np.ones((1,6))
cons=[]
for i in range(5):
    for j in range(i+1,6):
        cons.append({'type': 'ineq', 'fun': lambda x: np.abs(b0[i,j]+(x[i]+x[j])/2)-a0[i,j]})
res = minimize(obj, np.ones((1, 6)), constraints=cons, bounds=bd)
print(res)
