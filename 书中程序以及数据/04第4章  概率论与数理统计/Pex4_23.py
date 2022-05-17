#程序文件Pex4_23.py
import numpy as np
import pandas as pd
import statsmodels.api as sm
df = pd.read_excel("Pdata4_23.xlsx", header=None)
a=df.values.T.flatten()
b=np.arange(1,6)
x=np.tile(b,(4,1)).T.flatten()
d={'x':x,'y':a} #构造求解需要的字典
model = sm.formula.ols("y~C(x)",d).fit()  #构建模型
anovat = sm.stats.anova_lm(model)  #进行单因素方差分析
print(anovat)

