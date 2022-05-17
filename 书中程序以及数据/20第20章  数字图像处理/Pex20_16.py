# 程序文件Pex20_16.py
from PIL import Image, ImageFont, ImageDraw

a = Image.open("玉龙雪山.jpg").convert("RGBA")
b = Image.new("RGBA", a.size, (0, 0, 0, 0))  # (0,0,0,0)透明
fnt = ImageFont.truetype("simsun.ttc", 120)  # 设置字体
c = ImageDraw.Draw(b)  # 将新建的图像添入画板
c.text(
    (b.size[0] - 500, b.size[1] - 150), "玉龙雪山", font=fnt, fill=(255, 255, 255, 255)
)  # (255,255,255,255)为白色，不透明
d = Image.alpha_composite(a, b)  # 合并两个图像
d.show()
d.save("figure20_16.png")
