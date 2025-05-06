with open('sistema.log', 'r') as file:
    for line in file:
        if "Accepted password" in line:
            print(line.strip())
            