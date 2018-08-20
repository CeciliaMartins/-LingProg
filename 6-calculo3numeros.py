##6-Faça um Programa que peça 2 números inteiros e um número
##real. Calcule e mostre:

##- o produto do dobro do primeiro com metade do segundo .
##- a soma do triplo do primeiro com o terceiro.
##- o terceiro elevado ao cubo.

import math

inteiroN1 = int(input("Digite um numero inteiro: "))
inteiroN2 = int(input("Digite outro numero inteiro: "))
realN3 = int(input("Digite um número real: "))


produto = (inteiroN1 * 2) * (inteiroN2/2)

soma = (inteiroN1 * 3) + realN3

elevado = math.pow(realN3, 3)

mensagem =  "o produto do dobro do primeiro com metade do segundo, é :%i \nA soma do triplo do primeiro com o terceiro é: %f \nO terceiro elevado ao cubo é: %f" % (produto, soma, elevado)
print(mensagem)





    



