print("Número positivo,negativo,neutro")
for num in range(1,4):
    num = int(input("número"))
    if (num>0):
        print(num, "positivo")
    elif (num<0):
        print(num, "negativo")
    elif (num==0):
        print(num,"neutro")
