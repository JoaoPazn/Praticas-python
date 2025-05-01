import random

def Funcaosegundograu(A, B, C):
  functiontrue = "TRUE"  
  if not isinstance(A, (int, float)):
    print("VALOR NÃO FLOAT OU INTEGER")
    functiontrue = "FALSE"
    if not isinstance(B, (int, float)):
      print("VALOR NÃO FLOAT OU INTEGER") 
      functiontrue = "FALSE" 
    if not isinstance(C, (int, float)):
      print("VALOR NÃO FLOAT OU INTEGER")
      functiontrue = "FALSE"


  while functiontrue != "FALSE":
    baskhara = (B ** 2) -  (4*A*C)
    if baskhara < 0:
      print("NÃO HÁ RAIZES REAIS. DELTA MENOR QUE ZERO.") 
      return
    PrimeiroResultado = ((-B) + (baskhara ** 0.5)) / 2
    segundoResultado = ((-B) - (baskhara ** 0.5)) / 2
    PrimeiroResultado = str(PrimeiroResultado)
    segundoResultado = str(segundoResultado)
    print(PrimeiroResultado + ", " + segundoResultado)
    functiontrue = "FALSE"  

valor1 = int(input("Digite o valor de A :"))
valor2 = int(input("Digite o valor de B :"))
valor3 = int(input("Digite o valor de C :"))
print(valor1)
print(valor2)
print(valor3)

Funcaosegundograu(valor1, valor2, valor3)