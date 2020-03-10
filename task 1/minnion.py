import socket,pickle
port_min = 3008
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),port_min))
data =s.recv(9000)
data_arr = pickle.loads(data)
sum=0
for i in range(len(data_arr)):
    sum+=data_arr[i]
data_arr = pickle.dumps(sum)
s.send(data_arr)
s.close()
print(sum)

