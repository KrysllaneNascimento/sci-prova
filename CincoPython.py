notas = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
nomes = ['', '', '']

for i in range(0, 3):
    nomes[i] = input(f'Digite o nome do {i+1}º aluno: ')
    for j in range(0, 4):
        notas[i][j] = int((input(f'Digite a {j+1}º nota: ')))

maiorMedia = 0
indexAlunoMaiorMedia = 0
menorMedia = 0
indexAlunoMenorMedia = 0
for i in range(0, 3):
    soma = 0
    for j in range(0, 4):
        soma += notas[i][j]
    media = soma/len(notas[i])
    print(f'{nomes[i]} sua média foi {media}')
    if i == 0 or maiorMedia < media:
        maiorMedia = media
        indexAlunoMaiorMedia = i
    if i == 0 or menorMedia > media:
        menorMedia = media
        indexAlunoMenorMedia = i

print(f'O aluno com maior média foi {nomes[indexAlunoMaiorMedia]}')
print(f'O aluno com menor média foi {nomes[indexAlunoMenorMedia]}')