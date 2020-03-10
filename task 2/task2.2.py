from enum import Enum,unique
import threading,socket,time,pickle
@unique
class states(Enum):
    rest = 0
    up = 1
    down = 2
@unique
class states1(Enum):
    rr = 0
    ru = 1
    rd = 2
    ur = 3
    dr = 4
    ww = 5
class systerm():
    def __init__(self,list):
        self.list = list
        self.l1pos = 0
        self.l2pos = 0
        self.l1 = self.lift(list, 1, self.l1pos)
        self.l2 = self.lift(list, 2, self.l2pos)
        self.state2 = states1.rr
    def setst2(self):
        if(self.l1.state ==states.rest):
            if(self.l2.state ==states.rest):
                self.state2 = states1.rr
            elif(self.l2.state ==states.up):
                self.state2 = states1.ru
            elif (self.l2.state == states.down):
                self.state2 = states1.rd
        elif(self.l2.state ==states.rest):
            if (self.l1.state == states.up):
                self.state2 = states1.ur
            elif (self.l1.state == states.down):
                self.state2 = states1.dr
        else:
            self.state2 = states1.ww
    def settarget1(self):
        if(self.state2 == states1.rr):
            if (len(self.list)):
                min = 99999
                op = -1
                for x in range(len(self.list)):
                    if (min > abs((self.list[x])[0] - self.l1.pos)):
                        min = abs((self.list[x])[0] - self.l1.pos)
                        op = x
                self.l2.target = (self.list[op])[0]
                self.l2.setst()
                print(self.l2.state)
                self.setst2()
                print(self.state2)
                self.setst2()
        if(self.state2 == states1.rd):
            if(self.l1.pos >=self.l2.pos):
                if (len(self.list)):
                    min = 99999
                    op = -1
                    for x in range(len(self.list)):
                        if ((min > abs((self.list[x])[0] - self.l1.pos)) and (self.list[x])[0]>self.l2.pos) :
                            min = abs((self.list[x])[0] - self.l1.pos)
                            op = x
                    if(op==-1):
                        self.l1.state = states.rest
                    elif(abs((self.list[op])[0]-self.l1.pos)<=abs((self.list[op])[0]-self.l2.enpoint())):
                        self.l1.target = (self.list[op])[0]
                        self.l1.setst()
                        self.setst2()
                    else:
                        self.l1.state = states.rest
            else:
                if(len(self.list)):
                    min = 99999
                    op = -1
                    for x in range(len(self.list)):
                        if ((min > abs((self.list[x])[0] - self.l1.pos)) and ((self.list[x])[0]>self.l2.pos or (self.list[x])[1] =='u')):
                            min = abs((self.list[x])[0] - self.l1.pos)
                            op = x
                    if(op!=-1 and (abs((self.list[op])[0]-self.l1.pos)<=abs((self.list[op])[0]-self.l2.enpoint()))):
                        self.l1.target = (self.list[op])[0]
                        self.l1.setst()
                        self.setst2()
                    else:
                        self.l1.state = states.rest
        if (self.state2 == states1.dr):
            if (self.l2.pos >= self.l1.pos):
                if (len(self.list)):
                    min = 99999
                    op = -1
                    for x in range(len(self.list)):
                        if ((min > abs((self.list[x])[0] - self.l2.pos)) and (self.list[x])[0] > self.l1.pos):
                            min = abs((self.list[x])[0] - self.l2.pos)
                            op = x
                    if (op != -1 and (abs((self.list[op])[0]-self.l2.pos)<=abs((self.list[op])[0]-self.l1.enpoint()))):
                        self.l2.target = (self.list[op])[0]
                        self.l2.setst()
                        self.setst2()
                    else:
                        self.l2.state = states.rest
            else:
                if (len(self.list)):
                    min = 99999
                    op = -1
                    for x in range(len(self.list)):
                        if ((min > abs((self.list[x])[0] - self.l2.pos)) and (
                                (self.list[x])[0] > self.l1.pos or (self.list[x])[1] == 'u')):
                            min = abs((self.list[x])[0] - self.l2.pos)
                            op = x
                    if (op != -1 and (abs((self.list[op])[0]-self.l2.pos)<=abs((self.list[op])[0]-self.l1.enpoint()))):
                        self.l2.target = (self.list[op])[0]
                        self.l2.setst()
                        self.setst2()
                    else:
                        self.l2.state = states.rest
        if (self.state2 == states1.ru):
            if (self.l1.pos <= self.l2.pos):
                if (len(self.list)):
                    min = 99999
                    op = -1
                    for x in range(len(self.list)):
                        if ((min > abs((self.list[x])[0] - self.l1.pos)) and (self.list[x])[0] < self.l2.pos):
                            min = abs((self.list[x])[0] - self.l1.pos)
                            op = x
                    if (op != -1 and (abs((self.list[op])[0]-self.l1.pos)<=abs((self.list[op])[0]-self.l2.enpoint()))):
                        self.l1.target = (self.list[op])[0]
                        self.l1.setst()
                        self.setst2()
                    else:
                        self.l1.state = states.rest
            else:
                if (len(self.list)):
                    min = 99999
                    op = -1
                    for x in range(len(self.list)):
                        if ((min > abs((self.list[x])[0] - self.l1.pos)) and (
                                (self.list[x])[0] < self.l2.pos or (self.list[x])[1] == 'd')):
                            min = abs((self.list[x])[0] - self.l1.pos)
                            op = x
                    if (op != -1 and (abs((self.list[op])[0]-self.l1.pos)<=abs((self.list[op])[0]-self.l2.enpoint()))):
                        self.l1.target = (self.list[op])[0]
                        self.l1.setst()
                        self.setst2()
                    else:
                        self.l1.state = states.rest
        if (self.state2 == states1.ur):
            if (self.l2.pos <= self.l1.pos):
                if (len(self.list)):
                    min = 99999
                    op = -1
                    for x in range(len(self.list)):
                        if ((min > abs((self.list[x])[0] - self.l2.pos)) and (self.list[x])[0] < self.l1.pos):
                            min = abs((self.list[x])[0] - self.l2.pos)
                            op = x
                    if (op != -1 and (abs((self.list[op])[0]-self.l1.pos)<=abs((self.list[op])[0]-self.l2.enpoint()))):
                        self.l2.target = (self.list[op])[0]
                        self.l2.setst()
                        self.setst2()
                    else:
                        self.l2.state = states.rest
            else:
                if (len(self.list)):
                    min = 99999
                    op = -1
                    for x in range(len(self.list)):
                        if ((min > abs((self.list[x])[0] - self.l2.pos)) and ((self.list[x])[0] < self.l1.pos or (self.list[x])[1] == 'd')):
                            min = abs((self.list[x])[0] - self.l1.pos)
                            op = x
                    if (op != -1 and (abs((self.list[op])[0]-self.l2.pos)<=abs((self.list[op])[0]-self.l1.enpoint()))):
                        self.l2.target = (self.list[op])[0]
                        self.l2.setst()
                        self.setst2()
                    else:
                        self.l2.state = states.rest
    class lift():
        def __init__(self,list,ll,inpos):
            self.pos = inpos
            self.no = ll
            self.list1 = list
            self.state = states.rest
            self.path = []
            self.step = 0
            self.target = []
        def enpoint(self):
            max = 0
            i = -1
            en = 999999
            for x in range(len(self.path)):
                if(max<= abs((self.path[x])[2]-self.pos)):
                    max = abs((self.path[x])[2]-self.pos)
                    i = x
                    en = (self.path[i])[2]
            return en
        def cheakpick(self):
            l = len(self.list1)
            while (l):
                if (self.pos == (self.list1[l - 1])[0] and (((self.list1[l - 1])[1] == 'u' and self.state==states.up) or ((self.list1[l - 1])[1] == 'd' and self.state==states.down) or (self.state ==states.rest))):
                    self.path.append((self.list1[l - 1]))
                    print("pick up by lift {} at flour {}".format(self.no,self.pos))
                    self.list1.pop(l - 1)
                    self.settarget()
                l += -1
        def setst(self):
            if (self.target > self.pos):
                self.state = states.up
            elif (self.target < self.pos):
                self.state = states.down
        def drop(self):
            o = len(self.path)
            while (o):
                if (self.pos == (self.path[o - 1])[2]):
                    self.path.pop(o - 1)
                    print("Drop by lift {} at flour {}".format(self.no, self.pos))
                    self.settarget()
                o = o - 1
            if(len(self.path)==0):
                self.state = states.rest
        def settarget(self):
            if (len(self.path)):
                min = 99999
                op = -1
                for x in range(len(self.path)):
                    if (min > abs((self.path[x])[2] - self.pos)):
                        min = abs((self.path[x])[2] - self.pos)
                        op = x
                self.target = (self.path[op])[2]
                self.setst()
            else:
                self.cheaklen()
        def cheaklen(self):
            if(len(self.path)==0):
                self.state = states.rest
        def move(self):
            self.cheakpick()
            if(self.state == states.up):
                self.pos +=1
                self.step+=1
            elif(self.state == states.down):
                self.pos +=-1
                self.step+=1
            if (self.pos == self.target):
                self.drop()
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),4447))
s.listen(1)
clt, add = s.accept()
q = int(input("enter the number of inputs"))
inp = []
for x in range(q):
    ele = [int(input()),input(),int(input())]
    inp.append(ele)
final = systerm(inp)
lll=0
def interrupted():
    while (True):
        time.sleep(3)
        final.settarget1()
        final.l1.move()
        final.l2.move()
        final.setst2()
        if((lll==1)and not (len(final.list)  or len(final.l1.path) or len(final.l2.path))):
            break
    print(final.l1.step)
    print(final.l2.step)
def inpu():
    while True:
        global final
        data = clt.recv(4447)
        data_arr = pickle.loads(data)
        print(data_arr)
        if(data_arr[1]=='e'):
            lll=1
            break
        else:
            final.list.append(data_arr)
t1 = threading.Thread(target=interrupted,args=())
t1.start()
t2 = threading.Thread(target=inpu,args=())
t2.start()

