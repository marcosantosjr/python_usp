def main():

    n_binario = input()

    nb_reverso = ''

    n_decimal = 0

    expoente = 0

    for m in n_binario:
        if m == '0':
            n_decimal += 0 * 2 ** expoente
            expoente += 1
        elif m == '1':
            n_decimal += 1 * 2 ** expoente
            expoente += 1

    print(n_decimal)

main()