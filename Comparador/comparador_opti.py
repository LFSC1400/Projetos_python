'Otimização do código comparador.py'

from itertools import combinations

nomes = ["primeiro", "segundo", "terceiro"]


while True:
    numeros = [int(input(f"Escolha o {nomes[i]} número: ")) for i in range(3)]   
    '''Em vez de repetir int(input(...)) três vezes'''

    for (i, a), (j, b) in combinations(enumerate(numeros), 2):
        if a == b:
            print(f"O {nomes[i]} número é igual ao {nomes[j]}")

    menor, meio, maior = sorted(numeros)
    print(f"O maior valor é {maior}, o segundo maior é {meio}, e o menor é {menor}")
    '''Em vez de 6 if para cada ordem possível, e ainda funciona quando há valores repetidos'''


    if input("Deseja continuar? (S/N): ").upper() == "N":
        print("Arrivederci")
        break
    '''Jeito correto de finalizr ou repetir o programa, sem usar exec()'''

'''
sorted(): quando você compara todas as ordens possíveis, ordenar resolve de uma vez.
List comprehension: substitui linhas repetidas que só mudam um detalhe.
for + combinations: evita escrever cada par de comparação à mão.
while True + break: forma correta de repetir o programa.
'''