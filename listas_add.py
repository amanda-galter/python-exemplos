alunos=['Douglas']
alunos.append('rafael')
while True:
    nome= input('digite o nome do aluno:')
    alunos.append(nome)
    resposta= input('DEseja adicionar mais um aluno? (S/N):')
    if resposta.upper()=='N':
        break
print(f'alunos cadrastrados: {alunos}')