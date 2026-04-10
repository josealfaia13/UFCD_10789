prr = input("Escreva: ").lower()

match prr:
    case _ if prr in ("olá", "bom dia"):
        print("Saudação")
    case _ if prr.endswith("?"):
        print("Pergunta")
    case _ if "tchau" in prr or "adeus" in prr:
        print("Despedida")
    case _:
        print("Mensagem genérica")