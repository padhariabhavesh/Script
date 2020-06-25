# @ Author : Bhavesh Padhria
# Python Program to get IP Address

import socket

hostname = socket.gethostname()
IpAddress = socket.gethostbyname(hostname)

print(" Your Computer Name is : " + hostname)
print(" Your computer Ip Address is : " + IpAddress)




# Follow Me :  www.padharia.in

