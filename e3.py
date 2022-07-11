print("leia 3 nome, sexo, altura de 3 pessoas")
repetições = 3
for contador in range(repetições):
    nome = (input("Nome:"))
    sexo = (input("Sexo:"))
    altura = float(input("Altura"))
    if(sexo=="m"):
        print("Masculino")
    elif(sexo=="f"):
        print("Feminino")
        print("Nome:", nome)
        print("Altura:", altura)