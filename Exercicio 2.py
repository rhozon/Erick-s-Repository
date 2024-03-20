#equação

a = float (input("valor a: "))
b = float (input("vlaor b: "))
c = float (input("Valor c: "))

if a==0:
    print("valor invalido")

else:


    if b**2-4*a*c>0:
        print("Existem duas raízes distintas")
    elif b**2-4*a*c==0:
        print("Existem duas raízes iguais")
    elif b**2-4*a*c<0:
        print("existem duas raízes imaginárias conjulgadas")