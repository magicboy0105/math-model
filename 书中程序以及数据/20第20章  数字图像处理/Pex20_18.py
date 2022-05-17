#程序文件Pex20_18.py
import qrcode
qr=qrcode.QRCode(
    version=1, #二维码的尺寸大小，取值范围为1-40
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  #二维码里每个格子的像素大小
    border=5  #边框的格子厚度，默认是4
)
qr.add_data("https://www.python.org/")  #设置二维码数据
qr.make(fit=True)  #启用二维码颜色设置
img=qr.make_image(fill_color="green", back_color="white")
img.show(); img.save("figure20_17.png")  #显示并保存二维码
