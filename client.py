from socket import *
from threading import Lock
from concurrent.futures import ThreadPoolExecutor, as_completed
from constCS import SERVERS
import random
import time

print_lock = Lock()

# ====== CONFIG ======
NUM_RUNS = 10
MAX_WORKERS = 50  # adjust if needed

# ====== REQUEST GENERATION ======
def generate_request():
    a = random.uniform(-100, 100)
    b = random.uniform(-100, 100)
    op = random.randint(0, 3)

    if op == 3 and random.random() < 0.5:
        b = 0.0

    return a, b, op

# ====== SINGLE REQUEST ======
def send_request(a, b, op):
    host, port = random.choice(SERVERS)
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(5)

    start = time.perf_counter()

    try:
        s.connect((host, port))
        msg = f"{a} {b} {op}"
        s.sendall(msg.encode())

        data = s.recv(1024)
        end = time.perf_counter()

        if not data:
            raise RuntimeError("Empty response")

        payload = data.decode().strip()

        if "|" in payload:
            _, proc_time = payload.split("|", 1)
            proc_time = float(proc_time)
        else:
            proc_time = None

        return {
            "success": True,
            "rtt": end - start,
            "proc": proc_time
        }

    except:
        return {
            "success": False,
            "rtt": None,
            "proc": None
        }

    finally:
        s.close()

# ====== SINGLE RUN ======
def run_experiment(num_requests):
    stats = {
        "attempted": num_requests,
        "received": 0,
        "failed": 0,
        "total_rtt": 0.0,
        "total_proc": 0.0,
    }

    start_time = time.perf_counter()

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = []
        for _ in range(num_requests):
            a, b, op = generate_request()
            futures.append(executor.submit(send_request, a, b, op))

        for f in as_completed(futures):
            res = f.result()
            if res["success"]:
                stats["received"] += 1
                stats["total_rtt"] += res["rtt"]
                if res["proc"] is not None:
                    stats["total_proc"] += res["proc"]
            else:
                stats["failed"] += 1

    end_time = time.perf_counter()

    total_time = end_time - start_time
    avg_rtt = stats["total_rtt"] / stats["received"] if stats["received"] else 0
    avg_proc = stats["total_proc"] / stats["received"] if stats["received"] else 0
    loss_pct = (stats["failed"] / stats["attempted"]) * 100 if stats["attempted"] else 0

    return {
        "total_time": total_time,
        "avg_rtt": avg_rtt,
        "avg_proc": avg_proc,
        "loss_pct": loss_pct,
        "received": stats["received"]
    }

# ====== MAIN ======
def main():
    num_requests = int(input("Quantas requisições por execução? "))

    results = []

    for i in range(NUM_RUNS):
        print(f"\n=== Execução {i+1}/{NUM_RUNS} ===")
        res = run_experiment(num_requests)
        results.append(res)

        print(f"Tempo total: {res['total_time']:.4f}s")
        print(f"RTT médio: {res['avg_rtt']:.6f}s")
        print(f"Processamento médio: {res['avg_proc']:.6f}s")
        print(f"Perda: {res['loss_pct']:.2f}%")

    # ===== FINAL AVERAGE =====
    final = {
        "total_time": sum(r["total_time"] for r in results) / NUM_RUNS,
        "avg_rtt": sum(r["avg_rtt"] for r in results) / NUM_RUNS,
        "avg_proc": sum(r["avg_proc"] for r in results) / NUM_RUNS,
        "loss_pct": sum(r["loss_pct"] for r in results) / NUM_RUNS,
    }

    print("\n=== MÉDIA FINAL (10 execuções) ===")
    print(f"Tempo total médio: {final['total_time']:.4f}s")
    print(f"RTT médio geral: {final['avg_rtt']:.6f}s")
    print(f"Processamento médio geral: {final['avg_proc']:.6f}s")
    print(f"Perda média: {final['loss_pct']:.2f}%")

if __name__ == "__main__":
    main()
