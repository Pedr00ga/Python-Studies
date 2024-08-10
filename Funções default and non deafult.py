#Quantidade é default pois foi definida no momento da função
#Nome é não default pois pode ser definida quando puxar a função

def boas_vindas(Nome, Quantidade):
    print(f"Ola {Nome}")
    print(f"A quantidade é de {Quantidade} Notebooks")

boas_vindas(input("Digite o seu nome: "), input ("Digite a quantidade que deseja comprar: "))