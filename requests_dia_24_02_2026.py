import requests as re

pnome = ""
snome = ""
funcao = ""
max = ""
min = ""

pnome = input("Digite o seu e primeiro nome: \n")

snome = input ("Digite o seu ultimo nome: \n")

funcao = input("DIgite a sua função: \n")

max = int(input("Digite o id maximo que deseja: \n"))

min = int(input("Digite o id minimo que deseja: \n"))

if (max < min):
  print("Erro! Volte digitar")
  max = int(input("Digite o id maximo que deseja: \n"))
  min = int(input("Digite o id minimo que deseja: \n"))  

for i in range(min,max):
    requests= re.get(f"https://trainingserver.atec.pt/TrainingServer/Mulberry/JSON/Controls/Calendar/getCalendarDataSource.ashx?command=_SelectAllSchedulesDataSetGivenByUserId&oId={i}&idField=DataValueField&titleField=DataTextField&startDateField=DataStartField&endDateField=DataEndField&backgroundColorField=&textColorField=textcolor&eventColorField=color&description=description&picField=pic&urlField=url&start=1771804800&end=1772409600&_=1771937069151")

    if pnome in requests.text:
        if snome in requests.text:
          if f"Sessão como {funcao}" in requests.text:
              print(i,"request: ", requests.text, "\n")
              print(i, "Encontrado\n")
              break
    else:
        print("Não encontrado")