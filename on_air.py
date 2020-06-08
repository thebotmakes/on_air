import time
import unicornhat as unicorn
from Adafruit_IO import Client, RequestError, Feed
ADAFRUIT_IO_KEY = 'YOUR_IO_KEY'. # see the yellow 'Adafruit IO Key' link on the top left of the IO dashboard
ADAFRUIT_IO_USERNAME = 'YOUR_IO_USERNAME' # as above 
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
feed = aio.feeds('YOUR_FEED_NAME') # swap your_feed_name for whatever your IO feed is called
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
