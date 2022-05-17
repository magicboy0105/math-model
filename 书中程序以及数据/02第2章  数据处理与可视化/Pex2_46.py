#程序文件Pex2_46.py
from matplotlib.pyplot import plot, legend, xlabel, ylabel, savefig, show, rc
from scipy.stats import gamma
from numpy import linspace
x=linspace(0,15,100); rc('font',size=15); rc('text', usetex=True) 
plot(x,gamma.pdf(x,4,0,2),'r*-',label="$\\alpha=4, \\beta=2$")
plot(x,gamma.pdf(x,4,0,1),'bp-',label="$\\alpha=4, \\beta=1$")
plot(x,gamma.pdf(x,4,0,0.5),'.k-',label="$\\alpha=4, \\beta=0.5$")
plot(x,gamma.pdf(x,2,0,0.5),'>g-',label="$\\alpha=2, \\beta=0.5$")
legend(); xlabel('$x$'); ylabel('$f(x)$')
savefig("figure2_46.png",dpi=500); show()
