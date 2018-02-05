import sys
import getopt
import socket
import threading
from queue import Queue

print_lock = threading.Lock()

listen = False
command = False
target = ""
port = 0

def exit():
	print()
	sys.exit()

def tool_help():
	print()
	print("HCat tool - 1.0")
	print()
	print("Usage: hcat.py -t *target_address* -p *port*")
	print("      -p --port                            - set the port")
	print("      -t --target                          - set the target")
	print("      -l --listen                          - to listen on the *target-address* *port* for incomming connections")
	print("      -c --command                         - to start a command shell")
	print("      -h --help                            - to get help")
	print()
	print("args: use args using 'send_command'")
	print("      -s *file* --send *file*              - to send a file to the client ")
	print("      -r *file* --receive *file*           - to receive a file from the client")
	print("      -e *file* --execute *file*           - to execute a file on connection")

def error_arguments():
	print("Error in arguments...")
	print("Please try again...")
	print()
	tool_help()


def server_receive(connection):
	while(True):
		recv_len = 1
		data_received = ""
		while(recv_len):
			data = connection.recv(4096)
			data = data.decode()
			recv_len = len(data)
			data_received+=data
			if(recv_len<4096):
				break
		print(data_received)
		client_data = str.encode(data_received)
		print(client_data)


def server_send(connection):
	while(True):
		data_for_client = str.encode(input(">"))
		connection.send(data_for_client)

def start_server():
	global target,port
	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server.bind((target,port))
	server.listen(5)
	isConnected = False
	try:
		while(not isConnected):
			print("Waiting for connection...")
			connection, address = server.accept()
			print("Got connection from : ", address)
			isConnected= True
		try:
			t = threading.Thread(target=server_receive, args= (connection,))
			t.daemon = True
			t.start()
		except:
			print("Error starting receiving thread...")
		try:
			t = threading.Thread(target=server_send, args= (connection,))
			t.daemon = True
			t.start()
		except:
			print("Error starting sending thread...")

	except(KeyboardInterrupt):
		isConnected=False
		server.close()
		print("server closed..")


def start_client():
	global target,port
	print()
	print("Starting client...")
	print("Connecting to {} port {}".format(target,port))
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		client.connect((target,port))
		print("Connected...")
		while(True):
			cmd = input("> ")
			client.send(str.encode(cmd))
			recv_len = 1
			response = ""
			while(recv_len):
				data = client.recv(4096)
				data = data.decode()
				recv_len = len(data)
				response+=data
				if(recv_len<4096):
					break
			print(response)
	except: 
		print("Problems with the connection...")
		client.close()
		exit()


def main():
	global listen
	global command
	global port
	
	if not len(sys.argv[1:]):
		tool_help()
	
	try:
		opts, args = getopt.getopt(sys.argv[1:],"p:t:l:ch", ["port=","target=","listen","command","help"])
	except getopt.GetoptError as err:
		error_arguments()
	
	for opt,val in opts:
		if opt in ["-p","--port"]:
			port = int(val)
		elif opt in ["-t","--target"]:
			target = val
		elif opt in ["-l","--listen"]:
			listen = True
		elif opt in ["-c","--command"]:
			command = True
		elif opt in ["-h","--help"]:
			tool_help()
		else:
			error_arguments()

	
	if not listen and len(target) and port > 0:
		start_client()
	
	if listen:
		start_server()
	

main()

