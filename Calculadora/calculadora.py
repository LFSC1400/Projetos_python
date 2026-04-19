n1 = (int(input("Digite o primeiro número: ")))
n2 = (int(input("Digite o segundo número: ")))

operação = input("Sendo . a multiplicação" \
"/ a divisão " \
"+ a adição" \
"- a subtração" \
"Escolha a sua operação: ")

if operação == "/":
    if n1 == 0:
        print("Não é possível dividir por 0")
    if n2 == 0:
        print("Não é possível dividir por 0")    
    else:
        resultado = n1 / n2
        print(f"O resultado da divisão é: {resultado}")

if operação == ".":
    if n1 == 0:
        print("Quando um numero é multiplicado por 0, o resutado final é 0.")
    if n2 == 0:
        print("Quando um numero é multiplicado por 0, o resutado final é 0.")    
    else:
        resultado = n1 . n2
        print(f"O resultado da multiplicação é: {resultado}")

if operação == "+":
    resultado = n1 + n2
    print(f"O resultado da adição é: {resultado}")

if operação == "-":
    resultado = n1 - n2
    print(f"O resultado da subtração é: {resultado}")