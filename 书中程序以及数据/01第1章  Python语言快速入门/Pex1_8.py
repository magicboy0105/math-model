#程序文件Pex1_8.py
n=int(input("请输入n的值："))
def fac(n):
    if n<=1: return 1
    else: return n*fac(n-1)
m=fac(n)     #调用函数
print("%d!=%5d"%(n,m))


