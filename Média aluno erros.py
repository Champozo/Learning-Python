# Média aluno com tratamento de erros.
class Aluno(object):  
    def __init__(self,nome):
        self.nome = nome
        
    def inserir_notas(self,nota1,nota2):
        try:
            self.nota1 = float(nota1)
            self.nota2 = float(nota2)
        except ValueError:
            print('As notas devem ser números reais.')
    
    def calcular_media(self):
        try:
            return (self.nota1 + self.nota2) / 2
        except AttributeError:
            print('Não é possivel calcular a média sem inserir todas as notas.')
    
    def mostrar_informacoes(self):
        try:
            if (self.calcular_media() >= 6):        
                print(f'O aluno {self.nome} foi aprovado')
            else:
                print(f'O aluno {self.nome} foi reprovado')
        except TypeError:
            print('Não é possível mostrar informações até ter calculado a média')

aluno1 = Aluno('felipe')
aluno1.mostrar_informacoes()