#程序文件Pex20_20.py
import glob, numpy as np
from PIL import Image
f = glob.glob("附件1\\*.bmp")  #读入附件1下所有bmp文件名称
n = len(f); a = np.array(Image.open(f[0]))
a = a.astype(float); jj = np.arange(1,n)
L1 = a[:,0]; L2 = a[:,-1]  #拼接的大图像左边界和右边界初始化

tind = [0]
cont_img = a
for i in range(n - 1):
    tcha1 = [];     tcha2 = []
    for j in jj:
        a2 = np.array(Image.open(f[j])).astype(float)
        e1 = a2[:, 0]; e2 = a2[:, -1]
        cha1 = abs(L1 - e2).sum(); cha2 = abs(L2 - e1).sum()
        tcha1.append(cha1) ; tcha2.append(cha2)  #左右边界的差异
    m1 = np.array(tcha1).min(); m2 = np.array(tcha2).min()

    if abs(L1 - 255.).sum() < 1:
        ind = np.where(tcha2 == m2)
        tind=np.hstack((tind, jj[ind]))  # 右拼接
        tt = np.array(Image.open(f[jj[ind[0][0]]])).astype(float)
        cont_img = np.hstack((cont_img, tt))
        L2 = tt[:, -1]; np.delete(jj, ind)
    elif abs(L2 - 255.).sum() < 1:
        ind = np.where(tcha1 == m1)
        tind = np.hstack((jj[ind], tind)) # 左拼接
        tt = np.array(Image.open(f[jj[ind[0][0]]])).astype(float)
        cont_img = np.hstack((tt,cont_img))
        L1 = tt[:, 0]; np.delete(jj, ind)
    elif m1 < m2:
        ind = np.where(tcha1 == m1)
        tind = np.hstack((jj[ind], tind)) # 左拼接
        tt = np.array(Image.open(f[jj[ind[0][0]]])).astype(float)
        cont_img = np.hstack((tt, cont_img))
        L1 = tt[:, 0]; np.delete(jj, ind)
    else:
        ind = np.where(tcha2 == m2)
        tind=np.hstack((tind, jj[ind]))  # 右拼接
        tt = np.array(Image.open(f[jj[ind[0][0]]])).astype(float)
        cont_img = np.hstack((cont_img, tt))
        L2 = tt[:, -1]; np.delete(jj, ind)
print(tind)  #显示各个图像的拼接排列次序
Image.fromarray(cont_img).show()
