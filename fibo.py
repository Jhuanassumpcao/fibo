numero = 21 # número que se deseja verificar se pertence à sequência de Fibonacci

# inicialização das variáveis da sequência de Fibonacci
a = 0
b = 1

# cálculo da sequência de Fibonacci
while b < numero:
    a, b = b, a + b

# verificação se o número pertence à sequência de Fibonacci
if b == numero:
    print(numero, "pertence à sequência de Fibonacci")
else:
    print(numero, "não pertence à sequência de Fibonacci")
