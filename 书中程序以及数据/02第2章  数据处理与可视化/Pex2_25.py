#程序文件Pex2_25.py
f=open("Pdata2_25.txt","r")
s=f.read()
print(s)   #显示文件内容
n=0
for c in s:
    if c in "aeiouAEIOU": n+=1
print("元音的个数为：",n)

