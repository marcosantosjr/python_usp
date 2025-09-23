x = int(input('Digite um número: '))

if x <= 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    y = x * (x + 1) // 2  # Fórmula matemática para soma dos n primeiros números
    print(f"A soma dos {x} primeiros números inteiros positivos é: {y}")