#192.168.1.96
import CHIP_IO.GPIO as gpio
import socket

def set_pin(pin_num, on_off):
        pin_name = "XIO-P{}".format(pin_num)
        gpio.setup(pin_name, gpio.OUT)
        gpio.output(pin_name, int(on_off))
        gpio.cleanup(pin_name)

def handle_commands():
    while True:
            command = raw_input("command: ")
            commands = command.split(" ")
            if commands[0] == 'l':
                    set_pin(0, commands[1])
            if commands[0] == 'r':
                    set_pin(1, commands[1])

def run_command(command):
    commands = command.split(" ")
    print commands
    if commands[0] == 'l':
            set_pin(0, commands[1])
    if commands[0] == 'r':
            set_pin(1, commands[1])

#socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if __name__ == '__main__':
    handle_commands()