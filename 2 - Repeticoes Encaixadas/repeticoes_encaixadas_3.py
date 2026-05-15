# Dados dois naturais m e n determinar, entre todos os pares de números naturais (x,y) tais que x < m e y < n, um par para o qual o valor da expressão xy - x2 + y seja máximo e calcular também esse máximo.

#Entrada de dados
m = int(input("Digite m: "))
n = int(input("Digite n: "))

#Inicializaçõ das variáveis
valor_maximo = float('-inf') # Começa com o menor valor possível
par_maximo = (0, 0)

#Percorre todos os pares (x, y) com x < m e y < n
for x in range(m):
    for y in range(n):
        #Calcula o valor da expressão: xy - x² + y
        valor = x * y - x**2 + y

        #Se encontrou um valor maior, atualiza o máximo e o par
        if valor > valor_maximo:
            valor_maximo = valor
            par_maximo = (x, y)

#Exibe os resultados
print(f"\nPar (x, y) que maximiza a expressão: ({par_maximo[0]}, {par_maximo[1]})")
print(f"Valor máximo da expressão: {valor_maximo}")