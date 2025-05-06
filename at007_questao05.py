success = 0
failed = 0

with open('sistema.log', 'r') as file:
    for line in file:
        if "Accepted password" in line:
            success += 1
        elif "Failed password" in line:
            failed += 1

print(f"Logins bem-sucedidos: {success}")
print(f"Logins falhados: {failed}")
