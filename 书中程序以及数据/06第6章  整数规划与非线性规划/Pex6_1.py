#程序文件Pex6_1.py
import cvxpy as cp
from numpy import array
c=array([40,90])  #定义目标向量
a=array([[9,7],[-7,-20]])  #定义约束矩阵
b=array([56,-70])  #定义约束条件的右边向量
x=cp.Variable(2,integer=True)  #定义两个整数决策变量
obj=cp.Minimize(c*x)  #构造目标函数
cons=[a*x<=b, x>=0]    #构造约束条件
prob=cp.Problem(obj, cons)  #构建问题模型
prob.solve(solver='GLPK_MI',verbose =True)  #求解问题
print("最优值为:",prob.value)
print("最优解为：\n",x.value)
