from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import photos

# ここを参考に、図形ではなく文字列を任意の場所に重ねられるようにしてみた
# https://togetter.com/li/1016292

#img1 = photos.pick_image()
img1 = photos.capture_image()
img1.convert('RGBA')
drawbuffer = ImageDraw.Draw(img1)

# フォントの指定は iOS 上の full path が必要なので適当なエラーを出させて確かめた
# ipa フォントは StaSh を使って wget してきて unzip 
font = ImageFont.truetype('/private/var/mobile/Containers/Shared/AppGroup/たぶんここがそれぞれの端末で違う/Pythonista3/Documents/ipag.ttf', 100)
# 座標は(横,縦)で指定
drawbuffer.text((20, 20), 'from Pythonista app @tenyawanya', fill='red', font=font )

# 他の画像を重ねたい時は以下をアンコメントして使ってる
#img2= Image.open('re2.png', 'r')
#img1.paste(img2, (680, 400), img2.split()[3])

saveit = photos.save_image(img1)

img1.show()
if saveit is True:
     print ("saved")
