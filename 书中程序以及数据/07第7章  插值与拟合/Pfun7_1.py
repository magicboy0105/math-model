#程序文件名Pfun7_1.py
def w(x, y, i, x0):
    p=1.0
    for j in range(len(x)):
        if j==i: continue
        p *= (x0-x[j]); p /= (x[i]-x[j])
    return p

def Lag_intp(x, y, x0):
    s=0
    for i in range(len(i)): s += w(x, y, i, x0)
    return s
