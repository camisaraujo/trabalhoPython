mat = []
# para cada linha de 0 ate 2
for i in range(3):
    # linha comeca vazia 
    l = []
    # para cada coluna de 0 ate 3
for j in range(4):
    # preencha colunas de linha i
    l.append(i*j)
    # adiciona linha na matriz
    mat.append(l)
print(mat)