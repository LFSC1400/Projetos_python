n1 = int(input("Escolha o primeiro numero: "))
n2 = int(input("Escolha o segundo numero: "))
n3 = int(input("Escolha o terceiro numero: "))


"""Valores iguais"""

if n1 == n2:
    print("O primeiro numero é igual ao segundo")

if n1 == n3:
    print("O primeiro numero é igual ao terceiro")

if n2 == n3:
    print("O segundo numero é igual ao terceiro")



"""Valores operacao"""

if n1 > n2 and n2 > n3:
    print(f"O maior valor é {n1}, o segundo maior é {n2}, e o menor é {n3}")

if n1 > n3 and n3 > n2:
    print(f"O maior valor é {n1}, o segundo maior é {n3}, e o menor é {n2}")


if n2 > n1 and n1 > n3:
    print(f"O maior valor é {n2}, o segundo maior é {n1}, e o menor é {n3}")

if n2 > n3 and n3 > n1:
    print(f"O maior valor é {n2}, o segundo maior é {n3}, e o menor é {n1}")


if n3 > n2 and n2 > n1:
    print(f"O maior valor é {n3}, o segundo maior é {n2}, e o menor é {n1}")

if n3 > n1 and n1 > n2:
    print(f"O maior valor é {n3}, o segundo maior é {n1}, e o menor é {n2}")



"""Valores operacao"""

loop = input("Deseja continuar? (S/N): ")

if loop.upper() == "N":
    print("Arivederchi")

else:
    exec(open("comparador.py").read())