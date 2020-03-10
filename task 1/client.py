import socket,pickle
port_gru =2018
port_sum = 2363
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),port_gru))
s.listen(1)
n=int(input("enter the number of element in array"))
l=[]
for i in range(n):
    l.append(int(input()))
clt , add =s.accept()
data_string = pickle.dumps(l)
clt.send(data_string)
clt.close()
s.close()
s3=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s3.bind((socket.gethostname(),port_sum))
s3.listen(1)
clt,add = s3.accept()
data1 =clt.recv(75)
data_arr1 = pickle.loads(data1)
print(data_arr1)
clt.close()
s3.close()





