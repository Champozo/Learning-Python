import random

def senha(n):
	maiuscula="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	minuscula="abcdefghijklmnopqrstuvwxyz"
	numeros="0123456789"
	especiais="~!@#$%^&*+_-=()[]/., "
	chars=[maiuscula,minuscula,numeros,especiais]
	res=""
	for i in range(int(n)):
		res+=random.choice(chars[random.randrange(0,4,1)])
	return res

def main():
	print("Bem vindo ao gerador de senhas!\n")
	lenght=input("Digite o tamanho da senha:\n")
	print("Sua senha é:\n")
	print(senha(lenght)+"\n")
main()
