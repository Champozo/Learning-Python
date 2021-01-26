# Calculadora com input
class Calculadora(object):
    def __init__(self,primeiro_valor,segundo_valor):
        self.primeiro_valor = primeiro_valor
        self.segundo_valor = segundo_valor
    
    def somar(self):
        soma = float(self.primeiro_valor) + float(self.segundo_valor)
        return soma
    def subtrair(self):
        subtracao = float(self.primeiro_valor) - float(self.segundo_valor)
        return subtracao
    def multiplicar(self):
        multiplicacao = float(self.primeiro_valor) * float(self.segundo_valor)
        return multiplicacao
    def dividir(self):
        divisao = float(self.primeiro_valor) / float(self.segundo_valor)
        return divisao

calculo = Calculadora(primeiro_valor=input(),segundo_valor=input())
calculo.dividir()
