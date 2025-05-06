import re

with open('sistema.log', 'r') as file:
    for line in file:
        if "ssh" in line.lower():
            ip = re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', line)
            if ip:
                print(ip.group())
                