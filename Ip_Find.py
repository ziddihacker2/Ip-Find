# pip3 install pyfiglet
import pyfiglet
banner1 = pyfiglet.figlet_format("Ip Find")
print(banner1)

## importing socket module
import socket
## getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)
## printing the hostname and ip_address
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")


