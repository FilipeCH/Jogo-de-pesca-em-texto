arquivo = open("data/peixe.txt", "r")
peixes = arquivo.readlines()



for index in range(len(peixes)):
    peixes[index] = peixes[index].rstrip("/n")
print(peixes)
arquivo.close()