# notas unicamp e pucpr

faculdade = float(input("Digite 1 - PUCPR \n 2 - UNICAMP:\n  "))

nota = float(input("Digite sua nota: "))

if faculdade ==1 and nota >=7.0:
    print("Aprovado")
elif faculdade ==1 and nota<=4.0 or nota <7.0:
    print("Em exame")
elif faculdade ==1 and nota<4:
    print("Reprovado")   

if faculdade ==2 and nota>=7.0:
    print("Aprovado")
elif faculdade ==2 and nota<5:
    print("Em exame")

