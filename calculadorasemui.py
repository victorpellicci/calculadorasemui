import time
while True:
     print("""Escolha uma das opções de operações a seguir, digitando o codigo da mesma:
0 - Parar a calculadora
1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Potenciação
6 - Radiciação
""")
     codigo=int(input())
     if (codigo==0):
         print("Obrigado por usar a calculadora do Victor")
         break
     if (codigo < 0 or codigo > 6):
         print("Codigo invalido")
         time.sleep(2)
         continue
     if (codigo==6):
         print("Escolha o radicando da operação")
         numero_um=int(input())
     else:
         print("Escolha o primeiro numero da operação")
         numero_um=int(input())
     if (codigo==6):
         print("Escolha o indice da operação (Ex: 2 se for quadrada)")
         numero_dois=int(input())
     else:
         print("Escolha o segundo numero da operação")
         numero_dois=int(input())
     if (codigo==1):
        print(numero_um+numero_dois)
     elif (codigo==2):
        print(numero_um-numero_dois)
     elif (codigo==3):
        print(numero_um*numero_dois)
     elif (codigo==4):
        print(numero_um/numero_dois)
     elif (codigo==5):
        print(numero_um**numero_dois)
     elif (codigo==6):
        print(numero_um**(1/numero_dois))
     time.sleep(3)
