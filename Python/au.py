arquivo = open("palavras.txt", "r")
for linha in arquivo:
    linha = arquivo.readline()
    print(linha)

arquivo.close()