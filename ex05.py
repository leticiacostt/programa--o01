#-----------------------------
#------ALGORITMO 119----------
#-----------------------------
a = float(input("Digite primeiro número: "))
b = float(input("Digite segundo número: "))
c = float(input("Digite terceiro número: "))

if a < c:
  a, c = c, a
if a < b:
  a, b = b, a
if b < c:
  b, c = c, b
print(f"A ordem decrescente é {a}, {b} e {c}.")