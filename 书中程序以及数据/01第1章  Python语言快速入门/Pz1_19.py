#程序文件Pz1_19.py
def change(data):
    data[0], data[1] = data[1], data[0]
    print("函数内交换位置后：",end='')
    for i in range(2): print("data[%d]=%2d"%(i,data[i]),end='\t')
data=[16, 25]    #主程序
print("原始数据为：",end='')
for i in range(2): print("data[%d]=%2d"%(i,data[i]),end='\t')
print("\n-------------------------------------------------------")
change(data)
print("\n-------------------------------------------------------")
print("排序后数据为：",end='')
for i in range(2): print("data[%d]=%2d"%(i,data[i]),end='\t')
      
