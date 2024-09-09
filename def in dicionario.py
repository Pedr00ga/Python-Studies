

def calculoaluno():
    aluno = {"nome": "nome", "idade": 1, "nota_final": "1", "aprovacao": True}
    aluno["nome"] = input("Digite o nome do aluno: ")
    aluno["idade"] = input("Digite o idade do aluno: ")
    aluno["nota_final"] = int(input("Digite a nota final do aluno: "))

    if aluno["nota_final"] >= 7:
        aluno["aprovacao"] = True

    else:
        aluno["aprovacao"] = False
    for keys, values in aluno.items():
        print(f"{keys}: {values}")

calculoaluno()
