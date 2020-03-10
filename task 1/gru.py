import threading,socket,time,pickle
port_gru =2018
port_min=3008
port_sum=2363
no = 0

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),port_gru))
s2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s2.bind((socket.gethostname(),port_min))
s2.listen(no)
no = int(input("enter the no of minion"))
# no = 2
# data = s.recv(4096)
# data_arr = pickle.loads(data)
# no = data
data = s.recv(4096)
data_arr = pickle.loads(data)
s.close()
n=len(data_arr)
print(n)
sum=0
w=n//no
v=n%no
print(w)
wen = []
for i in range(no):
    #sl=slice(i*w,(i+1)*w)
    #  v=v-
    wen.append([])
    for u in range(w):
       wen[i].append(data_arr[i*w+u])
       if(v):
           wen[i].append(data_arr[n-v])
           v=v-1
t = -1
def call():
    global t
    global sum
    t=t+1
    data_string = pickle.dumps(wen[t])
    clt, add = s2.accept()
    clt.send(data_string)
    dev = clt.recv(90)
    data_arr1 = pickle.loads(dev)
    sum = data_arr1 +sum
    clt.close()
for n in range(no):
    t1 = threading.Thread(target=call, args=())
    t1.start()
time.sleep(10)
s3=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s3.connect((socket.gethostname(),port_sum))
data_string = pickle.dumps(sum)
s3.send(data_string)
s3.close()

