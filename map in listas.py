

lista1 = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]

#def multiplica(x):
 #   return x * 9
multiplica = lambda x: x * 9

resultado = map (multiplica, lista1)

print(list(resultado))