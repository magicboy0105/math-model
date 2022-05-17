#程序文件Pex12_2_1.py
import numpy as np; import statsmodels.api as sm
a=np.loadtxt("Pdata12_1.txt")
#加载表中x1,x2,y的13行3列数据（数据见封底二维码）
d={'x1':a[:,0],'x2':a[:,1],'y':a[:,2]}
md=sm.formula.ols('y~x1+x2',d).fit()  #构建并拟合模型
print(md.summary(),'\n------------\n')  #显示模型所有信息
ypred=md.predict({'x1':a[:,0],'x2':a[:,1]})  #计算预测值
print(ypred)  #输出预测值


