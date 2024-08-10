idade = input("Digite a sua idade: ")
idade = int (idade)
MAIORDIDADE = 18
ADOLESCENTE = 13
VELHO = 100


if idade >= MAIORDIDADE:
    print("Você é maior de idade")
elif 18 < idade >= ADOLESCENTE: #substitui and para ficar mais limpo, porém mais complicado de ler
    print("Você é um adolescente")

else:
    print("Você é menor de idade")

while idade >= 0:
    idade += 1
    print(idade)
    if idade >= VELHO:
        break

if idade >= VELHO :
    print("Você morreu de velhice")


# == Equal
# != Not Equal
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to