#-----------------------------
#------ALGORITMO 97-----------
#-----------------------------
numero = int(input("Digite um número: "))

if (numero % 10) == 0:
  print("O número (",numero,") é múltiplo de 10")
else:
  if (numero % 5) == 0:
    print("O número (",numero,") é múltiplo de 5 ")
  else:
    if (numero % 2) == 0:
      print("O número (",numero,") é múltiplo 2")
    else:
      print("O número (",numero,") não é múltiplo de 10, de 5 e nem de 2")

