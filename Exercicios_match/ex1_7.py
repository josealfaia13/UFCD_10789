catg = input("Insira categoria(eletronico/alimento) do produto: ")
preco = int(input("Insira o valor do produto: "))

produto = {"categoria": catg, "preço": preco }

match produto:
    case {"categoria": "eletronico", "preço": p}if p > 1000:
        print("Produto de Luxo")
    case {"categoria": "eletronico", "preço": p}if p <= 1000:
        print("Produto comum")
    case {"categoria": "alimento", "preço": p}if p > 0:
        print("Produto alimentar")
    case _:
        print("categoria desconhecida")