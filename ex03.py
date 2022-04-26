#-----------------------------
#------ALGORITMO 100----------
#-----------------------------
#ler um número inteiro de 4 casas 
#e imprimir se é ou não múltiplo de 4 o número formado pelos algarismos 
#que estão nas casas das unidades de milhar e das de centenas
numero = int(input("Digite um número de 4 algarismos: "))

if (numero % 4) == 0:
  print("O número (",numero,") é múltiplo de 4")
else:
  print("O número (",numero,") não é múltiplo de 4")