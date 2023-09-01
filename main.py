from matriz import read_matrix
print("Escolha o labirinto (0-3):")
fileNumber = input()
fileName = 'labirintos/lab0' + str(fileNumber) +'.txt'
labirinto = read_matrix(fileName)
for row in labirinto:
    for val in row:
        print(val, end=" ")
    print()
