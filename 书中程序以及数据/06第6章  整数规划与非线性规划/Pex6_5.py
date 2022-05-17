#程序文件Pex6_5.py
from scipy.optimize import minimize
import numpy as np
c1=np.array([1,1,3,4,2]); c2=np.array([-8,-2,-3,-1,-2])
A=np.array([[1,1,1,1,1],[1,2,2,1,6],
            [2,1,6,0,0],[0,0,1,1,5]])
b=np.array([400,800,200,200])
obj=lambda x: np.dot(-c1,x**2)+np.dot(-c2,x)
cons={'type':'ineq','fun':lambda x:b-A@x}
bd=[(0,99) for i in range(A.shape[1])]
res=minimize(obj,np.ones(5)*90,constraints=cons,bounds=bd)
print(res)  #输出解的信息
