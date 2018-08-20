##10 Faça um programa que permita ao usuário digitar o seu nome e
##em seguida mostre o nome do usuário de trás para frente utilizando
##somente letras maiúsculas. Dica: lembre−se que ao informar o
##nome o usuário pode digitar letras maiúsculas ou minúsculas.
##Observação: não use loops.

nome = input("Digite o seu nome: ")

##Fatiamento
##Um substring de um string é chamado de fatia (do inglês slice).
##Selecionar uma fatia é semelhante a selecionar um caractere:
##print(nome[2:7]) "tela: cilia"
nomeAoContrario = nome.upper()
print(nomeAoContrario[::-1])
