#程序文件Pex4_24.py
import numpy as np
import statsmodels.api as sm
y=np.array([[11, 11, 13, 10], [10, 11, 9, 12],
         [9, 10, 7, 6], [7, 8, 11, 10],
         [5, 13, 12, 14], [11, 14, 13, 10]]).flatten()
A=np.tile(np.arange(1,5),(6,1)).flatten()
B=np.tile(np.arange(1,4).reshape(3,1),(1,8)).flatten()
d={'x1':A,'x2':B,'y':y}
model = sm.formula.ols("y~C(x1)+C(x2)+C(x1):C(x2)",d).fit()  #注意交互作用公式的写法
anovat = sm.stats.anova_lm(model)  #进行双因素方差分析
print(anovat)
