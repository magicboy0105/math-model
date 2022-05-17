# 程序文件Pan5_1_1.py
import matplotlib.pyplot as plt
from numpy import ones, diag, c_, zeros
from scipy.optimize import linprog

plt.rc("text", usetex=True)
plt.rc("font", size=16)
c = [-0.05, -0.27, -0.19, -0.185, -0.185]
A = c_[zeros(4), diag([0.025, 0.015, 0.055, 0.026])]
Aeq = [[1, 1.01, 1.02, 1.045, 1.065]]
beq = [1]
a = 0
aa = []
ss = []
while a < 0.05:
    b = ones(4) * a
    res = linprog(c, A, b, Aeq, beq)
    x = res.x
    Q = -res.fun
    aa.append(a)
    ss.append(Q)  # 把最优值都保存起来
    a = a + 0.001
plt.plot(aa, ss, "r*")
plt.xlabel("$a$")
plt.ylabel("$Q$", rotation=90)
plt.savefig("figure5_1_1.png", dpi=500)
plt.show()
