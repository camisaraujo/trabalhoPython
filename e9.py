print("Mostra nº de 5 a 100 divisíveis por 7, mas não mútiplo de 5")
for num in range(5,100):
    if(num % 7 == 0) and (num % 5 != 0):
        print(num)
