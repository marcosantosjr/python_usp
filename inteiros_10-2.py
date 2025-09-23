def main():

    n = int(input('Digite um número: '))

    i = 1

    while i * (i + 1) * (i + 2) < n:
        i += 1

    if i * (i + 1) * (i + 2) == n:
        print(f'{n} é triângular')
    else:
        print(f'{n} não é é triângular')

main()