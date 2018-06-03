import socket

chip_address = ('192.168.1.96', 5678)
chip_address = ('127.0.0.1', 5678)
con = None

try:
    sock = socket.socket()
    sock.connect(chip_address)
    while True:
        msg = raw_input('command wifi: ')
        sock.send(msg)
finally:
    sock.close()