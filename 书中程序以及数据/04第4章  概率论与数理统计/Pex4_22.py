#程序文件Pex4_22.py
import numpy as np
import statsmodels.api as sm
y=np.array([1620, 1670, 1700, 1750, 1800, 1580, 1600, 1640, 1720,
            1460, 1540, 1620, 1680, 1500, 1550, 1610])
x=np.hstack([np.ones(5), np.full(4,2), np.full(4,3), np.full(3,4)])
d= {'x':x,'y':y}   #构造字典
model = sm.formula.ols("y~C(x)",d).fit()   #构建模型
anovat = sm.stats.anova_lm(model)  #进行单因素方差分析
print(anovat)
