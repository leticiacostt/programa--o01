#-----------------------------
#------ALGORITMO 124----------
#-----------------------------
a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

if (a < b + c) and (b < a + c) and (c < a + b):
  if (a > b ) and (a > c):
    maior = (a ** 2)
    lados = (b **2 + c**2)
  else:
    if (b > c):
      maior = (b ** 2)
      lados = (a ** 2 + c **2)
    else:
      maior = (c ** 2)
      lados = (a ** 2 + b **2)
  if (maior == lados):
    print("Triângulo retângulo")
  else:
    if ( maior > lados ):
      print("Triângulo obtusângo")
    else:
      print("Triângulo acutângulo")
else:
  print("As medidas não formam um triângulo.")


