##11. Faça um programa que solicite a data de nascimento
##(dd/mm/aaaa) do usuário e imprima a data com o nome do mês por
##extenso.
##Data de Nascimento: 29/10/1973
##Você nasceu em 29 de Outubro de 1973.
##Obs.: Não use desvio condicional nem loops.
##mesExtenso = {1: "janeiro", 2 : "fevereiro", 3: "março", 4: "abril", 5: "maio"}
##dataNascimento = input("Digite sua data do seu nascimento")
##dia = dataNascimento[0:2]
##mes = dataNascimento[3:4]
##ano = dataNascimento[4:9]
##
##print ('Data nascimento: %s de %s de %s' % (dia, mesExtenso[int(mes)], ano))
#### 




mesExtenso = {1: "janeiro", 2 : "fevereiro", 3: "março", 4: "abril", 5: "maio"}
dataNascimento = input("Digite sua data do seu nascimento(dd/mm/yyyy)")
dia = int(dataNascimento[0:2])
mes = int(dataNascimento[3:4])
ano = int(dataNascimento[4:9])

print ('Data nascimento: %s de %s de %s' % (dia, mesExtenso[int(mes)], ano))



