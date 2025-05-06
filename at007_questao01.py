with open('sistema.log', 'r') as file:
    lines = file.readlines()
    print(f"Total de linhas no log: {len(lines)}")
    