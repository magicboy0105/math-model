#程序文件Pan8_1.py
import numpy as np
from scipy.integrate import odeint
s0=155.0;  i0=1.0;  s_inf=60.0;
sigma=(np.log(s0)-np.log(s_inf))/(s0+i0-s_inf)
print("sigma=",sigma)
S=np.array([155, 153, 139, 101])
I=(s0+i0)-S+1/sigma*np.log(S/s0)
print("所求的解为：\n",I)
