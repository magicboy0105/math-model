#程序文件名Pfun7_3.py
"""计算n阶差商 f[x0, x1, x2 ... xn]
输入参数：xi为所有插值节点的数组
输入参数：fi为所有插值节点函数值的数组
返回值:  返回xi的i阶差商(i为xi长度减1)"""
def diff_quo(xi=[], fi=[]):
    if len(xi)>2 and len(fi)>2:
        return (diff_quo(xi[:len(xi)-1],fi[:len(fi)-1])-diff_quo(xi[1:len(xi)],fi[1:len(fi)]))\
                /float(xi[0]-xi[-1])  #续行
    return (fi[0]- fi[1])/float(xi[0]-xi[1])
