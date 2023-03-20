quantidadeNumeros = 5
menorNumero = 0
maiorNumero = 0

for i in range(0, quantidadeNumeros):
    numero = float(input(f'Digite o {i+1}º número: '))
    if i == 0 or numero > maiorNumero:
        maiorNumero = numero
    if i == 0 or numero < menorNumero:
        menorNumero = numero

print(f'Maior Número: {maiorNumero}')
print(f'Menor Número: {menorNumero}')