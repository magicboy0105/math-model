#程序文件Pex7_9.py
import numpy as np
from scipy.optimize import curve_fit
x0=np.array([6, 2, 6, 7, 4, 2, 5, 9])
y0=np.array([4, 9, 5, 3, 8, 5, 8, 2])
z0=np.array([5, 2, 1, 9, 7, 4, 3, 3])
xy0=np.vstack((x0, y0))
def Pfun(t, a, b, c):
    return a*np.exp(b*t[0])+c*t[1]**2
popt, pcov=curve_fit(Pfun, xy0, z0)
print("a，b，c的拟合值为：", popt)
