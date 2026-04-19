from socket import *
from threading import Thread
from constCS import HOST, PORT
import time

def process_request(conn, addr):
    try:
        data = conn.recv(1024)
        if not data:
            return

        msg = data.decode().strip()
        print(f"[{addr}] Received: {msg}")

        start_proc = time.perf_counter()

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

        except Exception:
            result = "Invalid input format"

        proc_time = time.perf_counter() - start_proc
        response = f"{result}|{proc_time:.6f}"
        conn.sendall(response.encode())

    finally:
        conn.close()
        print(f"[{addr}] Connection closed")

def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(10)

    print(f"Server is running on {HOST}:{PORT}...")

    while True:
        conn, addr = s.accept()
        print("Connected by", addr)
        Thread(target=process_request, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    main()
