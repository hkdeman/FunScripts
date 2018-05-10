import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("10.17.202.80", 3333))
#s.connect(("localhost",3333))

try:
    while(True):
        # str_recv = s.recv(1024)

        # print(str(str_recv))

        str_send = input("Enter what you wanna tell your friend: \n")

        s.send(bytes(str_send, 'utf-8'))

        str_recv = s.recv(1024)

        print(str(str_recv.decode()))
except:
    print("Thanks for annoying the hell out of them!")
