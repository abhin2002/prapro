import psutil
import time

def print_cpu_usage():
    while True:
        print(f"CPU usage: {psutil.cpu_percent()}%")
        time.sleep(1)

print_cpu_usage()


