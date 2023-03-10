frutas = ["mamao", "morango", "uva", "banana"]
fruta_escolhida = "uva"
if (fruta_escolhida in frutas):
    print("A fruta {} está na lista no índice {}".format(fruta_escolhida, frutas.index(fruta_escolhida)))
else:
    print("fruta nao encontrada")