#程序文件名Pfun7_2.py
def diff_forward(f, k, h, x):
    if k<=0: return f(x)
    else: return diff_forward(f, k-1, h, x+h) - diff_forward(f, k-1, h, x)
