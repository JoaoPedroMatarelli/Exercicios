"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.



IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
"""


num = int(input("Digite um numero! "))
fib = 0
fib2 = 1
fib_valor = 0
while fib_valor < num:
    fib_valor = fib + fib2
    fib = fib2
    fib2 = fib_valor

if fib_valor == num:
    print("O valor pertecem a fibonacci")
elif num == 1 or num == 0:
    print("O valor esta na sequencia de fibonachi")
else:
    print("O valor não pertence a fibonacci")
