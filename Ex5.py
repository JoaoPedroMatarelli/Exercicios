"""
5) Escreva um programa que inverta os caracteres de um string.



IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;
"""


continuar = "s"
palavra = str(input("Digite uma palavra: "))
print(palavra[::-1])


while continuar == "s":
    continuar = str(input("""Deseja continuar\n
    [s] para continuar 
    [n] para encerrar
    """))    
    if continuar.lower() == "n":
        break
    elif continuar.lower() == "s":
        palavra = str(input("Digite uma palavra: "))
        print(palavra[::-1])        
    else:
        print("Erro!")
        break
