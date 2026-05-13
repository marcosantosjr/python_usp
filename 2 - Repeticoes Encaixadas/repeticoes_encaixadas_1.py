def main():
    # Lê o número n de sequências
    n = int(input("Digite o número de sequências: "))

    # Processa cada sequência
    for i in range(1, n + 1):
        soma_pares = 0

        print(f"\nSequência {i}:")

        # Lê os números da sequência até encontrar um 0
        while True:
            num = int(input("Digite um número (0 para terminar): "))

            if num == 0:
                break

            # Se o número dor par, adiciona à soma
            if num % 2 == 0:
                soma_pares += num

            # Exibe o resultado da sequência atual
            print(f"Soma dos números pares da sequência {i}: {soma_pares}")

if __name__ == '__main__':
    main()