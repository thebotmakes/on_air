# on_air
Code for a Raspberry PI Zero W powered on air indicator - a new essential for working at home!  Uses IFTHISTHENTHAT, Adafruit IO and a Pimoroni Unicorn PHAT.

Pre-requisites:
Set up the Pimoroni Unicorn library as per instructions here:
  https://github.com/pimoroni/unicorn-hat

I set up an Adafruit IO feed to store the state, which means you need to set up the Adafruit IO library as per instructions here:
  https://github.com/adafruit/Adafruit_IO_Python
(note - use the manual installation instructions rather than the easy installation option - for some reason the easy option didn't work for me but using the manual option worked straight away (and it's dead easy too!).

I wanted this up to work with my phone, so I used the IFTT (IfThisThenThat) app cause I knew I could link it up with an Adafruit IO feed easily.

How it works:

 * There's three 'states' - on air (do not disturb), busy (can be disturbed but would rather not be), off air (disturb me as   much as you want!)
 * I set up three button widgets with IFTT that post values to the IO feed (42 for on air (for no other reason than that was what was used in the Adafruit example code and I'm a Douglas Adams fan :-) ), 21 for busy, and 0 for off air.
 * The Python script running on the Pi Zero then monitors that feed and sets RGB values according to the state, then outputs that to the Unicorn PHAT.
 
Dead simple, and means I can change the state with one button press on my phone so easily done while on a video call without losing the track of the call.

Note - you need to run the code as root (so sudo python on_air.py from the terminal) - this is a requirement for the Unicorn library.  I have this set up to run automatically as soon as the Pi starts using the cron method here:  https://www.raspberrypi-spy.co.uk/2013/07/running-a-python-script-at-boot-using-cron/ .
