# a simple client socket
import socket
 
# define socket address
TCP_IP = '172.22.252.81'  # ip of the server we want to connect to
TCP_PORT = 4542  # port used for communicating with the server
BUFFER_SIZE = 1024  # buffer size used when receiving data
 
# create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket created successfully.")
 
# connect to server
s.connect((TCP_IP, TCP_PORT))
print ("Established connection with the server.")
print ("END to disconnect.")

while True:
	message = input("You: ")
	if message == "END":
		s.close()

	# send message to the server
	s.send(bytes(message, "utf-8")) 
 
	# receive data from server
	data = s.recv(BUFFER_SIZE)
	if data == "END":
		break
	print ("server: " + str(data, "utf-8"))

s.close()