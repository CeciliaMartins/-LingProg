##5 Faça um Programa que peça a temperatura em graus Celsius,
##transforme e mostre em graus Farenheit.


temperaturaC = int(input("Digite a temperatura em graus Celsius: "))

temperaturaF = (1.8 * temperaturaC + 32)

mensagem = "A temperatura %i em graus Celsius para graus Farenheit é %f" % (temperaturaC, temperaturaF)
print(mensagem)


    
