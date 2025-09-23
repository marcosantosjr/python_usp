def main():

    #números para o mdc
    n1 = int(input())
    n2 = int(input())

    #variáveis para armazenar o n1 e n2
    n1_r = n1
    n2_r = n2

    #resto entre n1 e n2, onde o n1 se torna o n2 e n2 se torna o resto
    y = n1 % n2

    while y != 0:
        n1 = n2
        n2 = y

        #quando y for 0 o n2 será o mdc
        y = n1 % n2

    print(f'O mdc entre {n1_r} e {n2_r} é {n2}')


main()