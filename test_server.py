import socket

address = ('', 67)
#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)
#a='111'

while True:
    #data, addr = s.recvfrom(2048)
    data, address= s.recvfrom(2048)
    print (data)
    print (address)
    #if not data:
    #    print("client has exist")
    #   break

   #print("received:", data, "from", addr)
   # print(s.recvfrom(2048))
s.close()
