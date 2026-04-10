jog1 = input("Jogador 1: ").lower()
jog2 = input("Jogador 2: ").lower()

match (jog1, jog2):
    case (jog1, jog2) if jog1 == jog2:
        print("Empate")
    case ("pedra", "tesoura"):
        print("Jogador 1 venceu")
    case ("tesoura", "papel"):
        print("Jogador 1 venceu")
    case ("papel", "pedra"):
        print("Jogador 1 venceu")
    case _:
        print("Jogador 2 venceu")