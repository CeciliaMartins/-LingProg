##9 Faça um programa que leia 2 strings e informe o conteúdo delas
##seguido do seu comprimento. Informe também se as duas strings
##possuem o mesmo comprimento e são iguais ou diferentes no
##conteúdo.
##Exemplo:
##String 1: Brasil Hexa 2018
##String 2: Brasil! Hexa 2018!
##Tamanho de "Brasil Hexa 2018": 16 caracteres
##Tamanho de "Brasil! Hexa 2018!": 18 caracteres
##As duas strings são de tamanhos diferentes.
##As duas strings possuem conteúdo diferente.

string1 = "Brasil Hexa 2018"
string2 = "Brasil! Hexa 2018!"


tamanhoString1 = len(string1)
tamanhoString2 = len(string2)

if(tamanhoString1 != tamanhoString2):
    print("As duas strings são de tamanhos diferentes.")
else:
    print("As duas strings são do mesmo tamanho.")
if(string1 != string2):
    print("As duas strings possuem conteúdo diferente.")
else:
    print("As duas strings possuem o mesmo conteúdo.")
    
