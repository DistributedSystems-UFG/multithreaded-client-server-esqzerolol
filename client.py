from socket import *
from constCS import *
import time

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))

# get user input
a = input("Enter first number: ")
b = input("Enter second number: ")
op = input("Operation (0=sum, 1=sub, 2=mult, 3=div): ")

msg = f"{a} {b} {op}"

# start timer
start_time = time.time()

s.send(msg.encode())

data = s.recv(1024)

# end timer
end_time = time.time()

result = data.decode()
elapsed_time = end_time - start_time

print("Result:", result)
print(f"Time taken: {elapsed_time:.6f} seconds")

s.close()
