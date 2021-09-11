import socket

LOCALHOST = 'localhost'

Connection = None

class SourceNode:
  def __init__(self, id):
    self.id = id

  def transmit(self, *value):
    Connection.socket.sendall(','.join(list(map(lambda x: str(x).encode(), value))))

class SinkNode:
  def __init__(self, id):
    self.id = id

  def retrieve(self, *value):
    data = ''
    while (byte := Connection.socket.recv(1)) != b'\n':
      data += byte.decode()
    return data.split(',')

class __IPC:
  def __init__(self, port):
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.socket.connect((LOCALHOST, port))

def connect(port):
  Connection = __IPC(port)
