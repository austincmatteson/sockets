import socket
import sys
from datetime import datetime
socket.getaddrinfo('127.0.0.1', 8888)
infos = socket.getaddrinfo('127.0.0.1', 8888)
stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]
socket.getaddrinfo('127.0.0.1', 8888)
client = socket.socket(*stream_info[:3])
client.connect(stream_info[-1])
if len(sys.argv) > 1:
    message = ' '.join(sys.argv[1:])
else:
    message = 'You did not send anything.'
buffer_length = 8
if len(message) == buffer_length:
    message += ' '
client.sendall(message.encode('utf8'))
message_complete = False
message = b''
while not message_complete:
    part = client.recv(buffer_length)
    message += part
    if len(part) < buffer_length:
        break
print('[{}] Echoed: {}'.format(datetime.now().strftime('%H:%M:%S %Y/%m/%d'),
                               message.decode('utf8')))
client.close()
