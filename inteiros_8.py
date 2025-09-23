def main():

      n = int(input('Digite um número inteiro não negativo para o fatorial: '))

      #número para multiplicar o fatorial
      n_i = n

      #número para o resultado do fatorial
      n_f = 1

      while n_i > 1:

          n_f *= n_i

          n_i -= 1

      print(f'Resultado do fatorial: {n_f}')


main()