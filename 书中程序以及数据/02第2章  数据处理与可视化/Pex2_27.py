#程序文件Pex2_27.py
import numpy as np
a = []; b = []; c = []
with open('Pdata2_21.txt') as file:
    for (i, line) in enumerate(file):
        elements = line.strip().split()
        if i < 6:
            a.append(list(map(float, elements[:8])))
            b.append(float(elements[-1].rstrip('kg')))
        else:
            c = [float(x) for x in elements]
a = np.array(a); b = np.array(b); c = np.array(c)
print(a,'\n',b,'\n',c)
