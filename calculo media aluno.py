#aluno calcular a media

media = float (input("informe sua média: " ))
if media>=7:
    print("aprovado!") 
elif media >=4 and media < 7:
    print("Exame final")
    diferenca = 7-media
    print(f"em exame por {diferenca: .2f} pontos")
else:
    print("se fudeu otario")

    