#programa para calcular imc
#redir para usuario peso(KG) e altura(m)
#calcular imc: peso/altura*altura)
#imprimir o IMC: "o seu IMC é: "

print("programa para calculo imc")
nome = input("informe seu nome: ")
peso = float(input("Informe seu peso: "))
altura = float(input("informe sua altura: "))
#processamento (cálculo)
imc = peso/(altura*altura)
#saída de dados
print(f"o atleta {nome} possuí o {imc:.3f}")

if imc>=28:
    print("ta gordo eim tiozao")    
