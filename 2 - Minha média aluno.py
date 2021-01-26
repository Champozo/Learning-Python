# Minha resolução:
class Aluno(object):
    def __init__(self,nome):
        self.nome = nome
    def inserir_nota(self):
        nota1 = float(input('Digite sua primeira nota: '))
        nota2 = float(input('Digite sua segunda nota: '))
        self.nota1 = nota1
        self.nota2 = nota2
        return self.calcular_media(nota1,nota2)
        
    def calcular_media(self,nota1,nota2):
        media = (nota1 + nota2) / 2
        self.media = media
        return media
    
    def mostrar_informacoes(self):
        if self.media >= 6:
            self.status = True
            print(f'O aluno {self.nome} foi aprovado com a média de: {self.media}')
        else:
            self.status = False
            print(f'O aluno {self.nome} foi reprovado com a média de {self.media}')
    
        
        
        
        
        
aluno1 = Aluno('Yuri')
aluno1.inserir_nota()
aluno1.mostrar_informacoes()
