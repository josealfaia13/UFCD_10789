dia_semana = input("Digite um dia da semana: ")

match dia_semana:
    case "segunda-feira":
        print("Dia útil")
    case "terça-feira":
        print("Dia útil")
    case "quarta-feira":
        print("Dia útil")
    case "quinta-feira":
        print("Dia útil")
    case "sexta-feira":
        print("Dia útil")
    case "sábado":
        print("fim-de-semana")
    case "domingo":
        print("fim-de-semana")
    case _:
        print("Erro!!")