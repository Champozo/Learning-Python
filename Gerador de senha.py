import random

# função para embaralhar e manter senha = str
def embaralhar(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#codigo principal
maiuscula1 = chr(random.randint(65,90)) #Baseado na tabela ASCII
maiuscula2 = chr(random.randint(65,90)) #Baseado na tabela ASCII
minuscula1 = chr(random.randint(97,122)) #Baseado na tabela ASCII
minuscula2 = chr(random.randint(97,122)) #Baseado na tabela ASCII
digito1 = chr(random.randint(48,57)) #Baseado na tabela ASCII
digito2 = chr(random.randint(48,57)) #Baseado na tabela ASCII

senha = maiuscula1 + maiuscula2 + minuscula1 + minuscula2 + digito1 + digito2 #junto todos caracteres gerados
senha = embaralhar(senha)#chamo a função com o parâmetro 'senha'

print(senha) #Output senha gerada