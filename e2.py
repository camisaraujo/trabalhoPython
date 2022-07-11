print("leia 3 valores e calcular a média")
n1 = float(input("n1"))
n2 = float(input("n2"))
n3 = float(input("n3"))
média = (n1 + n2 + n3/3)

print("Média:", média)
if (média<5.0):
    print("Reprovado")
elif (média>=7.0):
    print("Aprovado")
else:
    print("Recuperação")