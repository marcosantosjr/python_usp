n = 1

lista_notas = []

while n <= 10:
    nota = int(input())

    lista_notas.append(nota)
    n += 1

print(lista_notas)

#variáveis para determinar menor e maior nota
menor = 100
maior = 0

for i in lista_notas:
    if i < menor:
        menor = i

for j in lista_notas:
    if j > maior:
        maior = j

print(f'Menor nota: {menor}')
print(f'Maior nota: {maior}')