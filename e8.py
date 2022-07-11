print("Reajuste")
salario = float(input("Salário"))
if (salario>1000):
    salnovo = salario+(salario*0.05)
elif (salario>=500):
    salnovo = salario+(salario*0.10)
elif(salario<500):
    salnovo = salario+(salario*0.15)
print("Salário Novo:",salnovo)