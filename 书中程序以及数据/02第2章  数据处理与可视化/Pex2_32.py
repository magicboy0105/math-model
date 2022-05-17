#程序文件Pex2_32.py
import pandas as pd
a=pd.read_csv("Pdata2_32.txt",sep=',',parse_dates={'birthday':[0,1,2]},
  #parse_dates参数通过字典实现前三列的日期解析，并合并为新字段birthday
  skiprows=2,skipfooter=2,comment='#',thousands='&',engine='python')
print(a)
