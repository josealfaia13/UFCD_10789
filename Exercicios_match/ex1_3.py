tipo = input("Tipo (compra/venda): ")
valor = float(input("Valor: "))

pedido = {"tipo": tipo, "valor": valor}

match pedido:
    case {"tipo": "compra", "valor": valor}:
         print(f"Compra de {valor}€")
    case {"tipo": "venda", "valor": valor}:
        print(f"Venda de {valor}€")
    case _:
        print("Pedido desconhecido")

