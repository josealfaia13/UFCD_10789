opc = 0
saida = True 

while True:
    print("1 - Para receber um bom dia")
    print("2 - Para receber um boa tarde")
    print("3 - Para receber um boa noite")
    print("4 - Sair")
    opc = int(input("Introduza a opção"))

    match opc:
        case 1:
            print("Bom Dia")
        case 2:
            print("Boa Tarde")
        case 3:
            print("Boa noite")
        case 4:
            print("Adeus")
            break
    