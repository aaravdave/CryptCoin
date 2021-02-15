import socket


def connect(site):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
      server.connect((f'{site}.com' , 80))
      server.sendall(f'GET / HTTP/1.1\r\nHost: {site}.com\r\nAccept: text/html\r\n\r\n'.encode('UTF-8'))
      print(str(server.recv(4096), 'utf-8'))
