import os
escolha1 = 0
escolha2 = 0
recomecar = ""

while True:
    escolha1 = int(input("Escolha um Pedra(1), Papel(2)ou Tesoura(3): "))
    os.system('cls')
    escolha2 = int(input("Escolha um Pedra(1), Papel(2) ou Tesoura(3): "))
    os.system('cls')

    match escolha1:
        case 1:
            match escolha2:
                case 1:
                    print("Pedra é igual Pedra, logo é empate")
                case 2:
                    print("Pedra perde para o Papel, logo o segundo player ")
                case 3:
                    print("Pedra ganha a tesoura, logo primero player ganha")
                case _:
                    print("Escolha Errada")
        case 2:
            match escolha2:
                case 1:
                    print("Papel ganha a Pedra, logo o primeiro player ganha")
                case 2:
                    print("Papel é igual Papel, logo é empate")
                case 3:
                    print("Papel perde para a Tesoura, logo o segundo player ganha")
                case _:
                    print("Escolha Errada")
        case 3:
            match escolha2:
                case 1:
                    print("Tesoura perde para a Pedra, logo o segundo player ganha")
                case 2:
                    print("Tesoura ganha ao Papel, logo o primeiro player ganha")
                case 3:
                    print("Tesoura é igual a Tesoura, logo é empate")
                case _:
                    print("Escolha Errada")
        case _:
            print("Escolha Errada")

    recomecar = input("Deseja recomeçar (s/n)")
    if recomecar == "s":
        continue
    elif recomecar == "n":
        break
            
       
 
