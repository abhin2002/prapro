import psutil
import time

def print_cpu_and_network_usage():
    while True:
        # Get CPU usage
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f'CPU Usage: {cpu_usage}%')

        # Get network usage
        net_io = psutil.net_io_counters()
        bytes_sent = net_io.bytes_sent
        bytes_recv = net_io.bytes_recv
        print(f'Network Usage: Sent = {bytes_sent}, Received = {bytes_recv}')

        # Sleep for a bit before getting the next reading
        time.sleep(5)

print_cpu_and_network_usage()
