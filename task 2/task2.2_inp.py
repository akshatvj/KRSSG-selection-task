import socket,pickle
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),4447))
print("enter the inputs here and for end the program enter input (0,e,0)")
while True:
    ele = [int(input()),input(),int(input())]
    data_arr = pickle.dumps(ele)
    s.send(data_arr)
    if(ele[1]=='e'):
        break

