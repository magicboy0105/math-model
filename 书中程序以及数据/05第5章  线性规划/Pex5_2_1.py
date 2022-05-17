from scipy.optimize import linprog
c=[-1, 2, 3]; A = [[-2, 1, 1], [3, -1, -2]]
b=[[9], [-4]]; Aeq=[[4, -2, -1]]; beq=[-6]
LB=[-10, 0, None];
UB=[None]*len(c)  #生成3个None的列表
bound=tuple(zip(LB, UB))  #生成决策向量界限的元组
res=linprog(c,A,b,Aeq,beq,bound)
print("目标函数的最小值：",res.fun)
print("最优解为：",res.x)
