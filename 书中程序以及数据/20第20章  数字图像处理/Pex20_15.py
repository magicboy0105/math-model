#程序文件Pex20_15.py
from PIL import Image,ImageDraw,ImageFont
from numpy.random import randint,random

def rndChar():  #产生随机字符
    s="abcdefghjkmnpqrstuwxyABCDEFGHJKMNPRSTUWXY23456789@#$%&"
    #去除易混淆的字符
    return s[randint(0,len(s))]

def rndColor():  #生成随机颜色
    return tuple(randint(64,256,3))

w=50*6; h=60  #设置图像的宽度和高度
a=Image.new('RGB',(w,h),(255,255,255))
font=ImageFont.truetype("c:\\Windows\\Fonts\\simsun.ttc",48)
b=ImageDraw.Draw(a)  #创建Draw对象

def createLines(n):  #绘制干扰线
    for i in range(n):
        begin=(randint(0,w),randint(0,h))  #起始点
        end=(randint(0,w),randint(0,h))    #结束点
        b.line([begin,end],fill=rndColor(),width=2)

def createPoints(rate):  #绘制干扰点
    for x in range(w):
        for y in range(h):
            if random(1)<=rate:
                b.point((x,y),fill=rndColor())

def drawStr():  #绘制字符
    Str=''
    for t in range(6):
        Chr=rndChar(); Str=Str+Chr
        b.text((50*t+10,5),Chr,font=font,fill=rndColor())
    print(Str)

createLines(6); createPoints(0.15); drawStr()
a.show(); a.save("figure20_15.png")





        
