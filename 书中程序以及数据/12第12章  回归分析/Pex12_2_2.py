#程序文件Pex12_2_2.py
import numpy as np; import statsmodels.api as sm
a=np.loadtxt("Pdata12_1.txt")
#加载表中x1,x2,y的13行3列数据（数据见封底二维码）
X = sm.add_constant(a[:,:2])  #增加第一列全部元素为1得到增广矩阵
md=sm.OLS(a[:,2],X).fit()  #构建并拟合模型
print(md.params,'\n------------\n')  #提取所有回归系数
y=md.predict(X)      #求已知自变量值的预测值
print(md.summary2())  #输出模型的所有结果
