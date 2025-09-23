while True:
    try:
        x = int(input())
        if x != 0:
            print(f'O quadrado de {x} é {x**2}')
        else:
            print('Fim')
            break
    except ValueError:
        print("Por favor, digite um número inteiro válido.")