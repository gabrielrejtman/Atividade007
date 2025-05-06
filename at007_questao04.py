with open('sistema.log', 'r') as file:
    for line in file:
        if "Failed password" in line:
            print(line.strip())
            