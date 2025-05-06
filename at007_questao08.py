from collections import defaultdict

failed_logins = defaultdict(int)

with open('sistema.log', 'r') as file:
    for line in file:
        if "Failed password" in line:
            parts = line.split()
            print(parts[8])
            user = parts[8]  # Ajuste o índice conforme necessário
            failed_logins[user] += 1

for user, count in failed_logins.items():
     if count > 1:
         print(f"Usuário: {user}, Falhas: {count}")
