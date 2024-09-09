

lista1 = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]


def multiplica(x):
    result = x * 9
    return result

def remover20(result):
    result2 = result > 20
    return result2
#multiplica = lambda x: x * 9


resultado = map (multiplica, lista1)

resultadolista = (list(resultado))

#print(list(resultado))

resultados = filter(remover20, resultadolista)

resultadoslista = list(resultados)

print(resultadolista)
print(resultadoslista)