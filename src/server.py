import socket
from datetime import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
print(sock)
address = '127.0.0.1'
port = 8888
sock.bind((address, port))
print(sock)
try:
    sock.listen(1)
    print('--- Starting server on port {} at {} ---'.format(port,
          datetime.now().strftime('%H:%M:%S %Y/%m/%d')))
    conn, addr = sock.accept()
    buffer_length = 8
    message_complete = False
    message = b''
    while not message_complete:
        part = conn.recv(buffer_length)
        message += part
        if len(part) < buffer_length:
            break
    print('[{}] Echoed: {}'.format(datetime.now()
          .strftime('%H:%M:%S %Y/%m/%d'), message.decode('utf8')))
    conn.sendall(message)
    conn.close()
    sock.close()
    print('--- Stopping server on port {} at {} ---'.format(port,
          datetime.now().strftime('%H:%M:%S %Y/%m/%d')))
except KeyboardInterrupt:
    try:
        conn.close()
    except NameError:
        pass
    sock.close()
    print('--- Stopping server on port {} at {} ---'.format(port,
          datetime.now().strftime('%H:%M:%S %Y/%m/%d')))
