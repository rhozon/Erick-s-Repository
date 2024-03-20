#condicional peso ideal

altura = float (input("Digite sua altura: "))
sexo = input("Qual seu sexo?: ")

a = (72.7*altura)-58
b = (62.1*altura)-44.7

if sexo==("masculino"):
    input(a)
elif sexo==("feminino"):
    input(b)