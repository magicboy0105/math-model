#程序文件Pex20_19.py
from PIL import Image
import qrcode
qr=qrcode.QRCode(
    version=2, 
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,  
    border=1
)
qr.add_data("https://www.python.org/") 
qr.make(fit=True) 
img=qr.make_image().convert("RGBA")
w1,h1=img.size
factor=4; w2=w1//factor; h2=h1//factor

icon=Image.open("logo.jpg")
w3,h3=icon.size
if w3>w2: w3=w2
if h3>w2: h3=h2
icon=icon.resize((w3,h3))  #更改图标的尺寸
w4=(w1-w3)//2; h4=(h1-h3)//2
img.paste(icon,(w4,h4))  #将图标粘贴到二维码的中心位置
img.show(); img.save("figure20_19.png")
    


