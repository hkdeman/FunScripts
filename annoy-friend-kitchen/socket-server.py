import socket
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate',150)  #120 words per minute
engine.setProperty('volume',0.9) 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 3333))

s.listen(5)
flag = 0
try:
    connect, addr = s.accept()
    print("Connection Address:" + str(addr))
    while True:
        # str_return = "Welcome to visit my test socket server. Waiting for command."
        # connect.sendto(bytes(str_return, 'utf-8'), addr)
        str_recv, temp = connect.recvfrom(1024)
    
        engine.say(str_recv.decode())

        engine.runAndWait()
        
        str_return = "Done!"
        connect.sendto(bytes(str_return, 'utf-8'), addr)
except:
    connect.close()
    s.close()
    print("Connection closed...")