#程序文件Pex5_6.py
import cvxpy as cp
import numpy as np
import pandas as pd
d1=pd.read_excel("Pdata5_6.xlsx",header=None)
d2=d1.values; c=d2[:-1,:-1]
d=d2[-1,:-1].reshape(1,-1); e=d2[:-1,-1].reshape(-1,1)
x=cp.Variable((6,8))
obj=cp.Minimize(cp.sum(cp.multiply(c,x)))  #构造目标函数
con=[cp.sum(x,axis=1,keepdims=True)<=e,
cp.sum(x,axis=0,keepdims=True)==d,x>=0]  #构造约束条件
prob=cp.Problem(obj,con)  #构造模型
prob.solve(solver='GLPK_MI',verbose =True)    #求解模型
print("最优值为：",prob.value)
print("最优解为：\n",x.value)

