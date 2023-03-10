import random

def jogar():

    print("****************************************")
    print("*** Bem vindo ao jogo da adivinhacao ***")
    print("****************************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Escolha um nível de dificuldade:")
    print("(1) Fácil - (2) Médio - (3) Difícil")

    nivel = int(input("Digite o nível desejado:"))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        chute = int(chute_str)
        if(chute<1 or chute>100):
            print("Você deve digitar um número entre 1 e 100 \n")
            continue

        print("Você digitou o número: ", chute_str, "\n")

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!\n".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior que o número secreto!\n")
                if(rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {} \n".format(numero_secreto, pontos))
            elif(menor):
                print("Você errou! O seu chute foi menor que o número secreto!\n")
                if(rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {} \n".format(numero_secreto, pontos))
                    print("Você errou! O seu chute foi menor que o número secreto!\n")
            pontos_perdidos = abs(numero_secreto - chute) # funcao abs() é do valor absoluto (como se fosse em modulo)
            pontos = pontos - pontos_perdidos
    print("*** Fim de Jogo ***\n\n")

if(__name__ == "__main__"):
    jogar()