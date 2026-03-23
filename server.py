from socket import *
from constCS import *

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print("Server is running...")

(conn, addr) = s.accept()
print("Connected by", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break

    msg = data.decode()
    print("Received:", msg)

    try:
        parts = msg.split()
        a = float(parts[0])
        b = float(parts[1])
        op = int(parts[2])

        if op == 0:
            result = a + b
        elif op == 1:
            result = a - b
        elif op == 2:
            result = a * b
        elif op == 3:
            if b == 0:
                result = "Error: division by zero"
            else:
                result = a / b
        else:
            result = "Invalid operation"

    except:
        result = "Invalid input format"

    conn.send(str(result).encode())

conn.close()
