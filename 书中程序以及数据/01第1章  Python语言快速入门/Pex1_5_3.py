#程序文件Pex1_5_3.py
def factorial(n):
    r = 1
    while n > 1: r *= n; n -= 1
    return r
print(factorial(5))  #调用函数
