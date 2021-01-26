# Calculadora simples com tratamento de erro
class Calculadora(object):
    def soma(self,primeiro_valor,segundo_valor):
        return primeiro_valor + segundo_valor
    def subtracao(self,primeiro_valor,segundo_valor):
        return primeiro_valor - segundo_valor
    def multiplicacao(self,primeiro_valor,segundo_valor):
        return primeiro_valor * segundo_valor
    def divisao(self,primeiro_valor,segundo_valor):
        try:
            return primeiro_valor / segundo_valor
        except ZeroDivisionError:
            print('Você não pode dividir por zero.')
calc = Calculadora()
print(calc.soma(5,5))
print(calc.subtracao(10,10))
print(calc.multiplicacao(5,25))
print(calc.divisao(100,10))
print(calc.divisao(10,0))
