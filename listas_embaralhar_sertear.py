import random
alunos=['Amanda',"Bianca",'Carlos', 'Diana', 'Evelyn' ]
print(f"lista:{alunos}")
#embaralhar a lista
random.shuffle(alunos)
print(f'lista embaralhada: {alunos}')
#ordenar a lista crescente
alunos.sort()
print(f'lista crescente: {alunos}')
#ordenar a lista decrescente
alunos.sort(reverse=True)
print(f'lista decrescente: {alunos}')