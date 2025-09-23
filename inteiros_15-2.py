def main():

    n = int(input())
    m = int(input())
    j = int(input())

    i = 1

    while i < n:

        if n % i == j % i:
            print(i)

        i += 1

main()