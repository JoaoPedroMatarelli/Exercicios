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
