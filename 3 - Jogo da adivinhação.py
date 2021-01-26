import random
intervalo = []
for i in range(0,101):
    intervalo.append(i)
print('Bem vindo ao jogo da adivinhação!')
nome = input('Por favor digite seu nome: ')
while True:
    if nome == '':
        print('Seu nome não pode ficar em branco.')
        nome = input('Por favor digite seu nome: ')
    else:
        break
print(f'Bem vindo {nome}, ao jogo da adivinhação! O jogo funciona assim: ')
print('Eu escolhi um número entre 0 e 100. Você vai tentar adivinhar meu número chutando. Você tem 7 chutes.')
print('Quando você chutar eu vou te dizer se você tem que chutar um número maior ou menor.')
print('Vamos começar. Boa sorte :D')

def jogar_novamente():
    while True:
        escolha = input('Quer jogar novamente? ')
        if escolha == 'sim':
            chute()
        elif escolha == 'não':
            print('Foi bom jogar com você, se cuide!')
            break
        else:
            print('Eu não entendi. Por favor digite \'sim\' ou \'não\' ')


def chute():
    numero = random.randint(0,101)
    chutes = 7
    resposta = int(input('Seu chute é: '))

    while chutes < 8 and chutes > 1:
        while True:
            if resposta not in intervalo:
                print('Sua resposta não é valida. Por favor digite um número entre 0 e 100.')
                resposta = int(input('Seu chute é: '))
            else:
                break
        if resposta == numero:
            print('Boaaaaaaaa, você acertou. Como você conseguiu? :O')
            jogar_novamente()
            break

        elif resposta > numero:
            print('Chutou alto demais. Tente um número menor.')
            chutes -= 1

            print(f'Agora lhe restam: {chutes} chutes')
            resposta = int(input('Seu chute é: '))

        else:
            print('Esse é seu melhor chute? Tente um número maior.')
            chutes -= 1

            print(f'Agora lhe restam: {chutes} chutes')
            resposta = int(input('Seu chute é: '))
    if chutes == 1:
        print(f'Erroooooooou feio, errooooooooou rude. O número era {numero}.')
        jogar_novamente()

chute()
