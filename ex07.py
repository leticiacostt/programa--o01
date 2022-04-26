#-----------------------------
#------ALGORITMO 123----------
#-----------------------------
a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

if (a < b + c) and (b < b + c) and (c < a + c):
  if (a == b) and (a == c):
    print("Triângulo equilátero")
  else:
    if (a == b) or (a == c) or (b == c):
      print("Triângulo isósceles")
    else:
      print("Triângulo escaleno")
else:
  print("As medidas não formam um triângulo")
