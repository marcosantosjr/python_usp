def main():

    n = int(input('Ditite um número: '))

    #verifica se o número é triângular
    i = 2

    #conta quantas vezes o número é triângular
    cont = 0

    while i < n / 2:
        if n % i == 0:
            cont += 1
        i += 1

    if cont == 0:
        print(f'{n} é primo')
    else:
        print(f'{n} não é primo')

main()