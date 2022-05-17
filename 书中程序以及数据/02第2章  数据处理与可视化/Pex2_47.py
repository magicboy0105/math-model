#程序文件Pex2_47.py
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
mu0 = [-1, 0]; s0 = [0.5, 1]
x = np.linspace(-7, 7, 100); plt.rc('font',size=15)
plt.rc('text', usetex=True); plt.rc('axes',unicode_minus=False)
f, ax = plt.subplots(len(mu0), len(s0), sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        mu = mu0[i]; s = s0[j]
        y = norm(mu, s).pdf(x)
        ax[i,j].plot(x, y)
        ax[i,j].plot(1,0,label="$\\mu$ = {:3.2f}\n$\\sigma$ = {:3.2f}".format(mu,s))
        ax[i,j].legend(fontsize=12)
ax[1,1].set_xlabel('$x$')
ax[0,0].set_ylabel('pdf($x$)')
plt.savefig('figure2_47.png'); plt.show()
