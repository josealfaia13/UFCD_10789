
nota = int(input("Insira uma nota(0-100): "))

match nota:
     case _ if nota >= 90 and nota <=100:
                print("Muito bom")
     case _ if nota >= 70 and nota <90:
                print("Bom")
     case _ if nota >= 50 and nota <70:
                print("Suficiente")
     case _ if nota >= 0 and nota < 50:
                print("Insuficiente")
     case _:
                print("Erro!")

     