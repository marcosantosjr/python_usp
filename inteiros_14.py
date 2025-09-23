def main():

    n = int(input())

    n1 = 1
    total = 0

    for i in range(n):
        aux = total
        total += n1
        n1 = aux


    print(f'A posição {n} tem como número de fibonnaci {aux}')

main()