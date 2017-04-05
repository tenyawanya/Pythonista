from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import photos
import webbrowser
# 画像保存後に instagram を起動させたいので webbrowser も import することにした

# ここを参考に、図形ではなく文字列を任意の場所に重ねられるようにしてみた
# https://togetter.com/li/1016292

#img1 = photos.pick_image()
img1 = photos.capture_image()
img1.convert('RGBA')
drawbuffer = ImageDraw.Draw(img1)

# フォントの指定は iOS 上の full path が必要なので適当なエラーを出させて確かめた
# ipa フォントは StaSh を使って wget してきて unzip 
font = ImageFont.truetype('/private/var/mobile/Containers/Shared/AppGroup/たぶんここがそれぞれの端末で違う/Pythonista3/Documents/ipag.ttf', 100)
# 上の行は端末だけでなく、インストールするたびにユニークなものになるらしいので入れ直した時などは修正が必要
# 座標は(横,縦)で指定
drawbuffer.text((20, 20), 'from Pythonista app @tenyawanya', fill='red', font=font )

# 他の画像を重ねたい時は以下をアンコメントして使ってる
#img2= Image.open('re2.png', 'r')
#img1.paste(img2, (680, 400), img2.split()[3])

# 撮影した画像をそのまま保存する場合はアンコメント
#saveit = photos.save_image(img1)
#img1.show()
# ここまで

# 正方形の画像として保存したい場合
crop_img = img1.resize((0, 0, 3024, 3024))
saveit = photos.save_image(crop_img)
crop_img.show()
# ここまで
if saveit_re is True:
     print ("saved")
# 保存した画像をそのままインスタに投稿したいので以下を追加
insta = 'instagram://camera'
webbrowser.open(insta)
