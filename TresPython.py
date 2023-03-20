resposta = 'S'

while resposta == 'S':
    nome = input("Digite o nome do aluno(a): ")
    nota1 = float(input(f'Digite a 1º nota: '))
    nota2 = float(input(f'Digite a 2º nota: '))
    nota3 = float(input(f'Digite a 3º nota: '))
    nota4 = float(input(f'Digite a 4º nota: '))
    media = (nota1+nota2+nota3+nota4)/4
    if media > 6:
        print(f'{nome} sua média foi {media}, você esta aprovado.')
    else:
        print(f'{nome} sua média foi {media}, você esta reprovado.')
    resposta = input("Deseja inserir outro Aluno?\nDigite S ou N: ").upper()


