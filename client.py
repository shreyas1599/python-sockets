import socket 

def Main(): 

    node = input("What node is this?")
    routing_table = []

    if node == 'A':
        print("This is Node A")
        routing_table.append(['B','B'])
        routing_table.append(['C','B'])
        routing_table.append(['D','B'])
    elif node == 'B':
        print("This is Node B")
        routing_table.append(['A','A'])
        routing_table.append(['C','C'])
        routing_table.append(['D','D']) 
    elif node == 'C':
        print("This is Node C")
        routing_table.append(['B','B'])
        routing_table.append(['A','B'])
        routing_table.append(['D','B'])
    else:
        print("This is Node D")
        routing_table.append(['B','B'])
        routing_table.append(['C','B'])
        routing_table.append(['A','B'])

    host = '127.0.0.1'
    while True:
        choice = input("What do you want to send?")

        if choice == "text": 
            destination = input("What is the destination?")
            for row in routing_table:
                if row[0] == destination:
                    if row[1] == 'A':
                        port = 1024
                    if row[1] == 'B':
                        port = 1025
                    if row[1] == 'C':
                        port = 1026
                    if row[1] == 'D':
                        port = 1027

            message = input("What do you want to send")
            message = str(destination) + str(node) + '~' + message
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

            s.connect((host,port)) 
            s.send(message.encode('ascii')) 

            ans = input('\nDo you want to continue(y/n) :') 
            if ans == 'y': 
                s.close()
                continue
            else: 
                break
            s.close()

        elif choice == "file":
            destination = input("What is the destination?")
            for row in routing_table:
                if row[0] == destination:
                    if row[1] == 'A':
                        port = 1024
                    if row[1] == 'B':
                        port = 1025
                    if row[1] == 'C':
                        port = 1026
                    if row[1] == 'D':
                        port = 1027
 
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
            s.connect((host,port)) 

            filename = input("Enter filename:")
            file = open(filename,'r')
            file_pointer = file.read(1000)
            while (file_pointer):
                print (file_pointer)
                message = str(destination) + str(node) + '~' + file_pointer
                s.send(message.encode('ascii'))
                file_pointer = file.read(1000)
                if 0<len(file_pointer)<1000:
                    file_pointer+='$'
            file.close()
            s.close()
            choice = input("Do you want to continue (Y or N)")
            if(choice == 'Y'):
                continue
            else:
                break



if __name__ == '__main__': 
	Main() 
