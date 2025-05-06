from collections import defaultdict
import re

ip_counts = defaultdict(int)

with open('sistema.log', 'r') as file:
    for line in file:
        if "ssh" in line.lower():
            ip = re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', line)
            if ip:
                ip_counts[ip.group()] += 1

for ip, count in sorted(ip_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"IP: {ip}, Conexões: {count}")
