import random

escolha = input("Escolha CARA ou COROA: ").strip().upper()

if escolha not in {"CARA", "COROA"}:
    print("Você não escolheu CARA nem COROA. Tente novamente.")

else:
    resultado = random.choice(["CARA", "COROA"])
    print(f"Resultado: {resultado}")

    if escolha == resultado:
        print(f"Parabéns! Você escolheu {escolha} e o resultado foi {resultado}.")

    else:
        print(f"Vish... Você escolheu {escolha} e o resultado foi {resultado}.")