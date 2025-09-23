def main():

    n = int(input())

    #base para a fórmula x * (x + 1) * (x + 2)
    x = 1

    #verifica se n é triângular
    z = 1

    while z < n:

        z = x * (x + 1) * (x + 2)

        x += 1

    if z == n:
        print(f'{n} é triângular')

    else:
        print(f'{n} não é triângular')

main()