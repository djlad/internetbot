#192.168.1.96
import CHIP_IO.GPIO as gpio
import socket

class Pins():
    def __init__(self):
        self.setupPins = set()

    def set_pin(self, pin_num, on_off):
        pin_name = "XIO-P{}".format(pin_num)
        if not pin_name in self.setupPins:
                gpio.setup(pin_name, gpio.OUT)
        gpio.output(pin_name, int(on_off))
        # gpio.cleanup(pin_name)

def createPins():
    return Pins()