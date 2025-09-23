def main():

    n = int(input('Digite n: '))
    i = int(input('Digite i: '))
    j = int(input('Digite j: '))

    mult = i * j

    lista_mult = []

    cont = 0
    num = 0

    while cont < n:

        if num % i == 0:
            lista_mult.append(num)
            cont += 1

        elif num % j == 0:
            lista_mult.append(num)
            cont += 1

        elif num % mult == 0:
            lista_mult.append(num)
            cont += 1

        num += 1

    print(lista_mult)

main()