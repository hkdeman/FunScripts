import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1",5555))
s.listen(5)
c = None
try:
	while(True):
		   if c is None:
			   # Halts
			   print('[Waiting for connection...]')
			   c, addr = s.accept()
			   print ('Got connection from', addr)
		   else:
			   # Halts
			   print ('[Waiting for response...]')
			   print(c.recv(1024).decode())
			   q = input("Enter something to this client: ")
			   c.send(str.encode(q))
except(KeyboardInterrupt):
	s.close()
	print("server closed..")

