# Dado um número inteiro positivo n, determinar todos os inteiros entre 1 e n que são comprimento da hipotenusa de um triângulo retângulo com catetos inteiros.

import math

n = int(input("Digite n: "))

hipotenusas = []

for a in range(1, n + 1):
    for b in range(a, n + 1):
        c = math.sqrt(a*a + b*b)
        if c == int(c) and c <= n:
            if int(c) not in hipotenusas:
                hipotenusas.append(int(c))

print(sorted(hipotenusas))