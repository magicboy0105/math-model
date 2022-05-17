#程序文件Pex20_2.py
import cv2,os
os.mkdir("source")  #在当前目录下创建新目录source
video=cv2.VideoCapture("test.avi")
L=int(video.get(cv2.CAP_PROP_FRAME_COUNT))  #计算视频的帧数
for i in range(L-1):
    ret,frame=video.read()
    cv2.imshow('Frame',frame); cv2.waitKey(2)  #停顿2毫秒
    cv2.imwrite("source\\"+str(i)+".jpg",frame)
