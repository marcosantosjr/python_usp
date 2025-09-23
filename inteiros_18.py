def main():

    a = int(input())
    b = int(input())
    c = int(input())

    if a ** 2 == b ** 2 + c ** 2:
        print("É triângulo retângulo")

    elif b ** 2 == a ** 2 + c ** 2:
        print("É triângulo retângulo")

    elif c ** 2 == a ** 2 + b ** 2:
        print("É triângulo retângulo")

    else:
        print("Não é triêngulo retângulo")


main()