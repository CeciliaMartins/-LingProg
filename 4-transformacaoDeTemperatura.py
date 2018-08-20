##4 Faça um Programa que peça a temperatura em graus Farenheit,
##transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32)/9)


temperaturaF = int(input("Digite a temperatura em graus Farenheit: "))

temperaturaC = (5 * (temperaturaF-32)/9)

mensagem = "A temperatura %f em graus Farenheit para graus Celsius é  %f" %(temperaturaF,temperaturaC)
print(mensagem)

    
