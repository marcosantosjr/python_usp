def main():

    i = 1

    soma_pares = 0

    while i <= 10:

        n = int(input('Digite um número: '))

        if n % 2 == 0:
            soma_pares += n

        i += 1

    print(f'Soma dos números pares da sequência: {soma_pares}')

main()