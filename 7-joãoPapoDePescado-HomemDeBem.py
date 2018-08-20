##7 João Papo-de-Pescador, homem de bem, comprou um
##microcomputador para controlar o rendimento diário de seu
##trabalho. Toda vez que ele traz um peso de peixes maior que o
##estabelecido pelo regulamento de pesca do estado de São Paulo (50
##quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João
##precisa que você faça um programa que leia a variável peso (peso
##de peixes) e verifque se há excesso. Se houver, gravar na variável
##excesso e na variável multa o valor da multa que João deverá pagar.
##Caso contrário mostrar tais variáveis com o conteúdo ZERO.


pesoDePeixes = float(input("Digite o peso dos peixes: "))

if pesoDePeixes > 50.00:
    excesso = pesoDePeixes - 50.00
    multa = excesso * 4
else:
    excesso = 0
    multa   = 0
mensagem = "O excesso de peixes foi de %f , e o valor da multa foi de %F " % (excesso, multa)

print(mensagem)

    
