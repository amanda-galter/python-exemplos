import random
alunos=['Amanda',"Bianca",'Carlos', 'Diana', 'Evelyn' ]
print(f"lista:{alunos}")
#embaralhar a lista
random.shuffle(alunos)
print(f"lista embaralhada:{alunos}")
#escolha um aluno aleatóriamente
aluno_sorteado=random.choice(alunos)
print(f"aluno sorteado:{aluno_sorteado}")