#192.168.1.96
import CHIP_IO.GPIO as gpio
import socket

def set_pin(pin_num, on_off):
        pin_name = "XIO-P{}".format(pin_num)
        gpio.setup(pin_name, gpio.OUT)
        gpio.output(pin_name, int(on_off))
        gpio.cleanup(pin_name)