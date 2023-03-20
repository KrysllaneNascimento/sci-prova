quantidadeInsercao = 5
numerosPar = []
numerosImpar = []
total = 0

for i in range(0, quantidadeInsercao):
    numero = float(input(f'Digite o {i+1}º número: '))
    if numero % 2 == 0:
        numerosPar.append(numero)
    else:
        numerosImpar.append(numero)
    total += numero

print("Números Pares: ")
for i in numerosPar:
    print(int(i))

print("Números Ímpares: ")
for i in numerosImpar:
    print(int(i))

print(f'Média Geral: {total/quantidadeInsercao}')