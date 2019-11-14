import socket 
from _thread import *
import threading 
locker = threading.Lock() 
this_node = 'A'
start = 0
def threaded(c): 
    global start
    while True: 

        data = str(c.recv(1003))
        if len(data)==3:
            break
        node = data.split('~')[0]
        received_from = node[3]
        node = node[2]
        data = data.split('~')[1][:-1]
        if not data: 
            print('Bye') 
            locker.release() 
            break
        print("The message received is: ", data)
        print("Recevied from: ", received_from)
        
        if this_node != node:
            print("Sending it to node: ", node)
            if node == 'A':
                port = 1024
                host = '127.0.0.1'
            if node == 'C':
                port = 1026
                host = '127.0.0.1'
            if node == 'D':
                port = 1027
                host = '127.0.0.1'
            if start == 0:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((host,port)) 
                start = 1
            if data [len(data)-1] == "$":
                data = str(node) + str(this_node) + '~' + data
                s.send(data.encode('ascii'))
                print (data)
                break
            data = str(node) + str(this_node) + '~' + data
            s.send(data.encode('ascii')) 
            
    try:
        s.close()
    except:
        print("")
    c.close()
    start=0
    locker.release() 


def Main(): 
    node = input("what node is this?")
    global this_node
    this_node = node
    routing_table = []
    if node == 'A':
        print("This is Node A")
        port = 1024
        host = '127.0.0.1'
        routing_table.append(['B','B'])
        routing_table.append(['C','B'])
        routing_table.append(['D','B'])
    elif node == 'B':
        print("This is Node B")
        port = 1025
        host = '127.0.0.1'
        routing_table.append(['A','A'])
        routing_table.append(['C','C'])
        routing_table.append(['D','D']) 
    elif node == 'C':
        print("This is Node C")
        port = 1026
        host = '127.0.0.1'
        routing_table.append(['B','B'])
        routing_table.append(['A','B'])
        routing_table.append(['D','B'])
    else:
        print("This is Node D")
        port = 1027
        host = '127.0.0.1'
        routing_table.append(['B','B'])
        routing_table.append(['C','B'])
        routing_table.append(['A','B'])
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port))
    print("socket binded to port", port) 

    s.listen(5) 
    print("socket is listening") 

    while True: 
        c, addr = s.accept() 
        locker.acquire() 
        print('Connected to :', addr[0], ':', addr[1]) 
        start_new_thread(threaded, (c,)) 
    s.close() 


if __name__ == '__main__': 
    Main() 
