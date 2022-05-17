#程序文件Pex20_17.py
from PIL import Image
base=Image.open("flower.jpg").convert("RGBA")
watermark=Image.open("logo.jpg").convert("RGBA").resize((100,100))
width,height=base.size
mark_width,mark_height=watermark.size
position=(width-mark_width,height-mark_height)
transparent=Image.new('RGBA',(width, height),(0,0,0,0))
transparent.paste(base,(0,0))
transparent.paste(watermark,position,mask=watermark)
transparent.show()
transparent.save("figure20_17.png")
