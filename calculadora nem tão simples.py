n1 = float(input("Digite um número: "))
operador = input("Digite um operador(digite 'a' para parar de calcular): ")
n2 = float(input("Digite um número: "))
n1novo = 0
condição1 = 0
operador_anterior = 0
if operador == '+':
    resultado = n1+n2
elif operador == '-':
    resultado = n1-n2
elif operador == '*':
    resultado = n1*n2
elif operador == '/':
    resultado = n1/n2
elif operador == 'a':
    print("Você não digitou nenhum cálculo!")
while operador != 'a':
    operador_anterior = operador
    condição1 = 1
    operador = input("Digite um operador(digite 'a' para parar de calcular): ")
    if operador == 'a':
        break
    else:
        n2 = float(input("Digite um número: "))
        if operador == '+':
            resultado2 = resultado+n2
        elif operador == '-':
            resultado2 = resultado-n2
        elif operador == '*':
            resultado2 = resultado*n2
        elif operador == '/':
            resultado2 = resultado/n2
        n1novo = resultado
        resultado = resultado2
if operador!='a' or condição1 == 1:
    if n1novo == 0:
        print("O resultado de {}{}{} é {}!".format(n1,operador_anterior,n2,resultado))
    else:
        print("O resultado de {}{}{} é {}!".format(n1novo,operador_anterior,n2,resultado2))