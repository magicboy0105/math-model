#程序文件Pex4_25_2.py
import statsmodels.api as sm
x=[2.5, 3.9, 2.9, 2.4, 2.9, 0.8, 9.1, 0.8, 0.7,7.9,
   1.8, 1.9, 0.8, 6.5, 1.6, 5.8, 1.3, 1.2, 2.7]
y=[211, 167, 131, 191, 220, 297, 71, 211, 300, 107,
   167, 266, 277, 86, 207, 115, 285, 199, 172]
df={'x':x,'y':y}
res=sm.formula.ols('y~x',data=df).fit()
print(res.summary(),'\n')
ypred=res.predict(dict(x=8))
print('所求的预测值为:',list(ypred))
