valor = input("Introduz um valor: ")

match valor:
    case _ if valor.isdigit():
        print("Número inteiro")
    case _ if valor.replace(".", "", 1).isdigit() and "." in valor:
        print("Número decimal")
    case _ if valor.startswith("[") and valor.endswith("]"):
        print("Lista")
    case _ if valor.isdigit():
        print("String numérica")
    case str():
        print("String textual")
    case _:
        print("Tipo desconhecido")