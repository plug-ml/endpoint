import socket

LOCALHOST = 'localhost'

Connection = None

def transmit(data):
  Connection.sendall(('%s\n' % data).encode())

def transmit_list(data):
  transmit(','.join(list(map(str, data))))

def retrieve():
  data = ''
  while (byte := Connection.recv(1)) != b'\n':
    data += byte.decode()
  return data

def retrieve_list():
  data = retrieve()
  return data.split(',')

def retrieve_mapped_list(func):
  data = retrieve_list()
  return list(map(func, data))

def connect(port):
  global Connection
  Connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  Connection.connect((LOCALHOST, port))
