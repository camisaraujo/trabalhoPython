maioralt=0
menoralt=4
maiorpeso=0
menorpeso=600
rep=5
for cont in range(rep):
    peso = float(input("Peso:"))
    altura = float(input("Altura"))
    if(altura>maioralt):
        maioralt=altura
    if(altura<menoralt):
        menoralt=altura
    if(peso>maiorpeso):
        maiorpeso=peso
    if(peso<menorpeso):
        menorpeso=peso
print("Maior altura:", maioralt)
print("Menor altura:", menoralt)
print("Maior peso:", maiorpeso)
print("Menor peso:", menorpeso)