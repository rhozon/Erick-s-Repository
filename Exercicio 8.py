#Eleitor

idade = int(input("Informe sua idade: "))

if idade<16:
    print("não é eleitor")
elif idade >=16 and idade <=17:
    print("Eleitor facultativo")
else:
    print("eleitor obrigatorio")