import socket  
  
address = ('127.0.0.1', 31500)  
#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
s.bind(address)  
#a='111'
  
while True:  
    #data, addr = s.recvfrom(2048)  
    packet = s.recvfrom(65565)
    packet = packet[0]
    ip_header = packet[0:20]
    print(packet)
    #if not data:  
    #    print("client has exist") 
    #   break  

   #print("received:", data, "from", addr)
   # print(s.recvfrom(2048))
s.close()  