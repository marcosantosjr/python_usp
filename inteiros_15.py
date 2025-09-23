def main():

    '''
    Dizemos que um número i é congruente módulo m a j se i % m = j % m.

    Exemplo: 35 é congruente módulo 4 a 39, pois 35 % 4 = 3 = 39 % 4.

    Dados inteiros positivos n, j e m, imprimir os n primeiros naturais congruentes a j módulo m.
    '''

    n = int(input('n: '))
    j = int(input('j: '))
    m = int(input('m: '))

    print(f"Os {n} primeiros naturais congruentes a {j} modulo {m} sao: ", end="")

    count = 0  # Contador para o número de naturais encontrados
    i = 0  # Percorre os números naturais, começando do 0

    # Loop para encontrar e imprimir os n primeiros naturais congruentes
    while count < n:
        if i % m == j % m:
            print(f"{i}", end=" ")
            count += 1  # Incrementa o contador de naturais encontrados

        i += 1  # Passa para o próximo número natural

main()