def main():

    n = int(input())

    contador = 1
    max_div = n / 2
    total = 0

    while contador <= max_div:
        if n % contador == 0:
            total += contador
        contador += 1


    if total == n:
        print(f'{n} é um número perfeito')
    else:
        print(f'{n} não é um número perfeito')

main()