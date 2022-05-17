#程序文件Pex1_9.py
x,n=eval(input("请输入x和n的值："))
def p(x,n):
    if n==1: return x
    else: return x*(1-p(x,n-1))
v=p(x,n)     #调用函数
print("p(%d,%d)=%d"%(x,n,v))
