#程序文件Pex5_7.py
from scipy.optimize import linprog
c=[-72, -64]    #目标向量
A =[[1, 1],[12, 8]]; b=[[50],[480]]
bound=((0,100/3.0),(0,None))
res=linprog(c,A,b,None,None,bound,method='simplex',options={"disp": True})
print("求解结果如下：",res)



