def jogar():

    enforcou = False
    acertou = False
    erros = 0
    palavra_secreta = "banana"
    letras_acertadas = ["_" for letra in palavra_secreta]

    while(not enforcou and not acertou):
        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você ganhou!")
    if(enforcou):
        print("Você perdeu!")

if(__name__ == "__main__"):
    jogar()