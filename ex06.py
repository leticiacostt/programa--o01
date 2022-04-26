#-----------------------------
#------ALGORITMO 122----------
#-----------------------------
a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

if (a < b + c) and (b < a + c) and (c < a + b):
  print("Podem ser lados de um triângulo")
else:
  print("Não podem ser lados de um triângulo")
