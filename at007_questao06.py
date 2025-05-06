with open('sistema.log', 'r') as file:
    for line in file:
        if "sudo" in line and "COMMAND" in line:
            user = line.split()[7]  # ajuste conforme necessário
            print(user)
