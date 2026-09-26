import socket
import sys


print("Python Port Scanner")
print("----------------------")

target = input("Enter target IP (e.g. 127.0.0.1): ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

print("\nStarting scan...\n")
try:
    for port in range(start_port, end_port + 1):

         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         s.settimeout(0.5)

         result = s.connect_ex((target, port))
    
         if result == 0:
              print(f"\n Port {port} is OPEN")

              try:
                        banner = s.recv(1024).decode().strip()
                        if banner:
                               print(f" Banner: {banner}")

          
              except:
                    pass

         s.close()
         
    
except KeyboardInterrupt:
     print("\n Scan interrupted by user.")

