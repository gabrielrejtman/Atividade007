from datetime import datetime

logs = []

with open('sistema.log', 'r') as file:
    for line in file:
        parts = line.split()
        time_str = f"{parts[0]} {parts[1]} {parts[2]}"
        time_obj = datetime.strptime(time_str, '%b %d %H:%M:%S')
        logs.append((time_obj, line.strip()))

# Ordenar por horário
logs.sort(key=lambda x: x[0])

for log in logs:
    print(log[1])
