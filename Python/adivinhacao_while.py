print("****************")
print("Adivinhacao \n")
print("****************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número: ")

    print("Você digitou o número: ", chute_str, "\n")

    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Você acertou!\n")
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o número secreto!\n")
        elif(menor):
            print("Você errou! O seu chute foi menor que o número secreto!\n")
    rodada = rodada + 1
print("*** Fim de Jogo ***\n\n")