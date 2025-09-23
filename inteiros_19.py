def main():

    n = input().split()

    a = int(n[0])
    b = int(n[1])
    c = int(n[2])

    if a > b and a > c:
        if b > c:
            print(f'Números ordenados: {a} {b} {c}')

main()