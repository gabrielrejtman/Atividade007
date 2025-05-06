
with open('sistema.log', 'r') as file:
    for line in file:
        if "sudo" in line:
            sudo_line = line.split()
            print(sudo_line[13].replace("COMMAND=", ''))
