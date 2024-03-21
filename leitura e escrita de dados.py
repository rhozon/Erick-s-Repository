#atividade para leitura e escrita de dados (entrada e saida)
#pedir para o usuário informar o nome - tipo string 
nome = input("informe o seu nome: ")
#PEdir CPF - tipo str
cpf = input("informe seu CPF: ")
#Pedir telefone - tipo str
tel = input("infomre o seu telefone: ")
#Pedir idade - tipo int - precisamos converter o input
idade = int(input("Informe sua idade: "))

#Saída de dados
#imprimir nome
print("nome do paciente: " + nome)
#imprimir cpf
print("CPF do cliente " + cpf)
#imprimir tel
print("telefone do cliente "+ tel)
#imprimir idade
#print("idade do cliente " str (idade) + "anos")
print (f"nome: {nome} \nCPF: {cpf} \ntelefone: {tel} \nIdade: {idade}")
