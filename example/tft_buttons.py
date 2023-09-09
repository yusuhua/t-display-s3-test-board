# input pins for buttons: you will need to change these to match your wiring

from machine import Pin


class Buttons():
    def __init__(self):
        self.name = "t-display-s3"
        self.start = Pin(0, Pin.IN, Pin.PULL_UP)
        self.select = Pin(14, Pin.IN, Pin.PULL_UP)
        self.up = Pin(3, Pin.IN, Pin.PULL_UP)
        self.down = Pin(18, Pin.IN, Pin.PULL_UP)
        self.left = Pin(2, Pin.IN, Pin.PULL_UP)
        self.right = Pin(17, Pin.IN, Pin.PULL_UP)
        self.a = Pin(21, Pin.IN, Pin.PULL_UP)
        self.b = Pin(16, Pin.IN, Pin.PULL_UP)
