#crie dois vetores com nome e notas de 4 alunos
# mostre o nome e a nota dos alunos acima da média da turma
nomes = ['ana','pedro','josé','maria']
notas = [9,0,8,7,0,6,0]

#media da turma 
soma = 0
for nota in notas:
    soma += nota 
media = soma/len(notas)
print('média da turma:', media)
for i in range(len(notas)):
    if notas[i]>media:
        print('aluno com nota acima da media:', nomes[i]),'nota:', notas[i]