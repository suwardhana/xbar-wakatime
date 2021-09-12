#!/usr/bin/python
# coding=utf-8

# <xbar.title>Binance Price Ticker</xbar.title>
# <xbar.version>v1.0</xbar.version>
# <xbar.author>Gabriel Age</xbar.author>
# <xbar.author.github>agezao</xbar.author.github>
# <xbar.desc>Displays Binanc e's ticker price for configured coin pairs</xbar.desc>
# <xbar.image>https://i.imgur.com/zJsoTl8.jpg</xbar.image>
# <xbar.dependencies>python</xbar.dependencies>

import json
from urllib import urlopen

bitcoin_icon='iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAQAAABLCVATAAAACXBIWXMAABYlAAAWJQFJUiTwAAABY0lEQVRIx2P4z0AdyEBzg1DAdIYfQJgCZHmCWdsYMAFRBs0BC2UAWT5g1p6hbZAggwIcrgALVQNZSWDWAQY24g3qwRtJ/xgeMqxkCGJgotQgGLzAoEUdg/4zvGQQIxzYLAyODF/gQv0MlgwWDK4MOQxbgV5DKG0nLtZ2wIUykII2EMmoU8QZtAWrQQwMB+HiDygzaDNc/CQlBskwfIKLN5JrkAxDFsMTuOh9BiFSDXoHDI2HDB9RlJ1kECc2r20hkI5OMXhQxyAQzCTNoDJgaAgAvaLLEMkwn+EbkuLvDBLkR78yUoD/Z0gn3yAGhnwk5V2UGBRGLYNmICkvIGzQLqwG8TA0oJQAVvgMymcoYehg+AUXWgoM0kygWC/DbpQ4+89wjYERt0FiRNeNX4GlFJ505EykMacZDPGn7HwCBnxiOMcwjcGJcOEvzqADh2vBQk1AVhaYdZCBc7TKpqJBA9ZiAwDMH49EXcmY2QAAAABJRU5ErkJggg=='

#List here the symbols you want to keep track:
coin_symbols=['HOTUSDT']
#To get a list of available symbols check all the "symbol" attributes here:
#https://api.binance.com/api/v1/ticker/24hr

for coin_symbol in coin_symbols:
    url="https://api.binance.me/api/v1/ticker/24hr?symbol={}".format(coin_symbol)
    urlidrt = "https://api.binance.me/api/v1/ticker/24hr?symbol=USDTIDRT"
    payload=urlopen(url)
    payload2=urlopen(urlidrt)

    data = json.load(payload)
    dataidrt = json.load(payload2)

    last_price=data['lastPrice']
    last_price_idrt=dataidrt['bidPrice']
    rupiah = round(float(last_price)*float(last_price_idrt)) * 99 / 100
    price_variation=str(data['priceChangePercent']) + '%'

#    print('{} - {} : {} | templateImage={}'.format(coin_symbol, last_price, price_variation, bitcoin_icon))
    # print('{} : {} | templateImage={}'.format(rupiah, price_variation, bitcoin_icon))
    print('{} : {}'.format(rupiah, price_variation, bitcoin_icon))
