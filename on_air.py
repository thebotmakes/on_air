import time
import unicornhat as unicorn
from Adafruit_IO import Client, RequestError, Feed
ADAFRUIT_IO_KEY = 'f89c40192b744bffadc0278127960b06'
ADAFRUIT_IO_USERNAME = 'thebot'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
feed = aio.feeds('on-air')
while True:
    state = aio.receive(feed.key)
    print(state.value)
    if state.value == '42':
        r = 220
        g = 20
        b = 60
    elif state.value == '21':
        r = 255
        g = 153
        b = 51
    else:
        r = 51
        g = 255
        b = 51
    unicorn.set_layout(unicorn.PHAT)
    unicorn.rotation(0)
    unicorn.brightness(0.5)
    width,height=unicorn.get_shape()


    for y in range(height):
      for x in range(width):
        unicorn.set_pixel(x,y,r,g,b)
        unicorn.show()
        time.sleep(0.05)

    time.sleep(1)