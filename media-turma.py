qtdAlunos = int(input())

if qtdAlunos == 0:
    print("NÃO HOUVE PROCESSAMENTO")
    exit()

mediaTurma = 0
ct = 0
while ct < qtdAlunos:
    mediaAluno = float(input())
    if mediaAluno >= 6:
        print("PARABÉNS VOCÊ ESTÁ APROVADO")
    mediaTurma += mediaAluno/qtdAlunos
    ct += 1
print(mediaTurma)

