#程序文件Pz20_1.py
import cv2
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)
