valor = input("Digite o valor da compra: ")
valor = int(valor)

while valor >= 20:
    valor = (valor * 0.10) + valor

    print(f"O valor final do seu produto será de de R${valor}")
    break
