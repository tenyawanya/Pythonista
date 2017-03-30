#!python3
# coding: utf-8
# こちらの記事を参考に連続投稿できるようにした。
# http://qiita.com/yubais/items/dd143fe608ccad8e9f85
from requests_oauthlib import OAuth1Session

import pytz
tzJst = pytz.timezone("Asia/Tokyo")	# 投稿時間が日本時間にならなかったのでおまじないに書いてみてる。意味があるのかはわからない。

CK = 'Consumer Key'                             # Consumer Key
CS = 'Consumer Secret'         # Consumer Secret
AT = 'Access Token' # Access Token
AS = 'Accesss Token Secert'         # Accesss Token Secert

# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/update.json"

repeat = "y"
tweet = ""

while (repeat == "y"):
# 投稿入力
  tweet = input('tweet> ')
  
# ツイート本文
  params = u'status='+'{}'.format(tweet)

# OAuth認証で POST method で投稿
  twitter = OAuth1Session(CK, CS, AT, AS)
  req = twitter.post(url, params = params)

# レスポンスを確認
  if req.status_code == 200:
    print ("OK")
  else:
    print ("Error: %d" % req.status_code)
# 引き続き投稿するかの確認
  repeat = input('repeat? (y/n)>')
else:
    print("end")
