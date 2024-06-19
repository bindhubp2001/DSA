import qrcode 
from PIL import Image

# image = qr.make("https://www.youtube.com/watch?v=FOGRHBp6lvM&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl")
# image.save("You_tube_qrgen")

qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_H, box_size = 10, border = 4)
qr.add_data("https://www.youtube.com/watch?v=FOGRHBp6lvM&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl")
qr.make(fit= True)

image = qr.make_image(fill_color="red",back_color = "blue")
image.save("You_tube_qrgen.png")