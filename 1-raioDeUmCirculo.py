#1 Faça um Programa que peça o raio de um círculo, calcule e
#mostre sua área.

import math

raioDoCirculo = int(input("Digite o raio do círculo para saber sua área!"))

areaDoCirculo = math.pi * math.pow(raioDoCirculo,2);
mensagem = "A área do circulo é: %f" % areaDoCirculo

print(mensagem)

