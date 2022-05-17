#程序文件Pex4_2.py
from scipy.stats import norm
from pylab import plot,fill_between,show,text,savefig,rc 
from numpy import array, linspace, zeros
alpha=array([0.001, 0.005, 0.01, 0.025, 0.05, 0.10])
za=norm.ppf(1-alpha,0,1)  #求上alpha分位数
print("上alpha分位数分别为", za)
x=linspace(-4, 4, 100); y=norm.pdf(x, 0, 1)
rc('font',size=16); rc('text',usetex=True)
plot(x,y)  #画标准正态分布密度曲线
x2=linspace(za[-1],4,100); y2=norm.pdf(x2);
y1=[0]*len(x2)
fill_between(x2, y1, y2, color='r')  #y1,y2对应的点之间填充
plot([-4,4],[0,0])  #画水平线
text(1.9, 0.07, "$\\leftarrow\\alpha$=0.1")  #标注
savefig("figure4_2.png", dpi=500); show()
