real = float(input('Quanto dinheiro vc tem? R$: '))
cotacao = float(input('Qual a cotação atual do cotacao? '))
dolar = real / cotacao

print(f'Com R$: {real} você pode comprar U$: {dolar}')