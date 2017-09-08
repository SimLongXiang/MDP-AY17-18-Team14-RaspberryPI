import socket

s = socket.socket()
host = '172.22.252.81'
port = 1606

s.connect((host, port))
print(s.recv(1024))

while True:
	sentence = input('Enter your message (type END to disconnect):')
	if sentence != 'END':
		s.send(bytes(sentence,"utf-8"))
	else:
		print('Connection Closed.')
		s.send(bytes('Connection Closed.',"utf-8"))
		s.close()
		break