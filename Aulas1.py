# 1. Construa um algoritmo para calcular as raízes de uma equação do 2º grau (Ax² + Bx
# + C), sendo que os valores A, B e C são fornecidos pelo usuário (considere que a
# equação possui duas raízes reais)
# real = "sim"

# A = input("Digite o A na função de segundo Grau : ")
# A = float(A)
# B = input("Digite o B na função de segundo Grau : ")
# B = float(B)
# C = input("Digite o C na função de segundo Grau : ")
# C = float(C)

# while real != "nao":
#     bask = (B**2) -4*A*C

#     if bask < 0:
#         print("Resultados Não Serão Reais")
#         break

#     resultado1 = (-B + (bask**0.5))/ 2*A
#     resultado2 = (-B - (bask**0.5))/ 2*A

#     print(resultado1, resultado2, sep=",")

#     real = "nao"

# 2. Construa um algoritmo que, tendo como dados de entrada dois pontos quaisquer do
# plano cartesiano, P(x1, y1) e Q(x2, y2), imprima a distância entre eles.
# A fórmula que efetua o cálculo da distância entre dois pontos é:
# 𝑑 = (𝑥2 − 𝑥1)² + (𝑦2 − 𝑦1)²

# x1 = input("Digite o Valor do primeiro ponto no plano cartesiano")
# x1 = float(x1)
# y1 = input("Digite o Valor do segundo ponto no plano cartesiano")
# y1 = float(y1)

# x2 = input("Digite o Valor do terceiro ponto no plano cartesiano")
# x2 = float(x2)
# y2 = input("Digite o Valor do segundo ponto no plano cartesiano")
# y2 = float(y2)

# d = (x2 - x1)**2 + (y2 - y1)**2

# print(d)

# 3. Construa um algoritmo que permita fazer um levantamento do estoque de vinhos de
# uma adega, tendo como dados de entrada os tipos de vinho, sendo ‘T’, ‘B’ para
# branco e ‘R’ para rosé. Especifique a porcentagem de cada tipo sobre o total geral
# de vinhos. A quantidade de vinhos é desconhecida. Utilize como finalizador ‘F’.

# T = input("Digite a quantidade de vinhos brancos classificados como T")
# T = float(T)
# B = input("Digite a quantidade de vinhos brancos classificados como B")
# B = float(B)

# R = input("Digite a quantidade de vinhos Rosé")
# R = float(R)

# Total = T + B + R

# tperc = T / Total
# tperc = tperc * 100

# bperc = B / Total
# bperc = bperc * 100

# rperc = R / Total
# rperc = rperc * 100

# print('''Total = {}
#       Total de vinhos marcado como T = {}%
#       Total de vinhos marcado como B = {}%
#       Total de vinhos marcado como R = {}%'''.format(Total, tperc, bperc, rperc))