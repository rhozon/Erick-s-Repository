#Calculo de aposentadoria

idade = int(input("digite sua idade: "))
servico = int(input("seu tempo de serviço: "))

if idade>=65:
    print("Pode se aposentar")
elif servico>=30:
    print("Pode se aposentar")    
elif idade>= 60 and servico>=25:
    print("Pode se aposentar")
else:
    print("Não pode se aposentar")    
