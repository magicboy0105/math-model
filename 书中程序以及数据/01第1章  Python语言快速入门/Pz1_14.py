#程序文件Pz1_14.py
def square_sum(n, p=2):
    result=sum([i**p for i in range(1, n+1)])
    return (n, p, result)
print("1到%d的%d次方和为%d"%square_sum(10))
print("1到%d的%d次方和为%d"%square_sum(10,3))
