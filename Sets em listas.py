

#Utilizar sets em uma lista faz com que a mesma perca os valores de indexação

list1 = [10, 20, 30, 40, 50, 60, 70, 80]
list2 = [30, 40, 70, 90, 100]

num1 = set(list1)
num2 = set(list2)

print (num1 | num2) #Union mostra os valores das duas listas porém não mostra os duplicados 2 vezes

print (num1 - num2) #Difference mostra apenas os valores diferentes da lista 1
print (num2 - num1) #Mostra apenas os valores diferentes da lista 2

print (num1 & num2) #Apenas os valores duplicados das listas

print (num1 ^ num2) #Symetric Difference mostra apenas os valores diferentes da lista

print(len(num1)) #Verifica a quantidade de itens em uma lista