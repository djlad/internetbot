import socket
from pins import run_command

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 5678))
sock.listen(1)

while True:
    try:
        (con, address) = sock.accept()
        msg = con.recv(1024)
        print msg
        while msg != 'q':
            msg = con.recv(1024)
            print msg
    finally:
        con.close()
