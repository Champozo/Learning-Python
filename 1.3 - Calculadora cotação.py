print('Bem vindo a calculadora de cotação.')
try:
  real = float(input('Quanto dinheiro vc tem? R$: '))
except ValueError:
  print('Digite apenas números inteiros.')
  real = float(input('Quanto dinheiro vc tem? R$: '))
escolha = str(input('Que moeda gostaria de comprar? (dolar/euro)'))

if escolha == 'dolar':
    cotacao = float(input('Qual a cotação atual do dolar? '))
    dolar = real / cotacao
    print(f'Com R$: {real} você pode comprar U$: {dolar:.2f}')
elif escolha == 'euro':
    cotacao = float(input('Qual a cotação atual do euro? '))
    euro = real / cotacao
    print(f'Com R$: {real} você pode comprar €{euro:.2f}')
else:
    print('Não entendi. Por favor digite se quer comprar dolar ou euro.')

