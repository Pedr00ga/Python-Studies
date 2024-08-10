idade = input("Digite a sua idade: ")
idade = int(idade)
Pode_votar = 18

#if idade >= Pode_votar:
   # print("Você pode votar")

#else:
   #print("Você não pode votar")

resultado = "Você pode votar" if idade >= Pode_votar else "Você não pode votar"

print(resultado)