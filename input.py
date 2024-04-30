# Entrada de Dados
aluno = input('digite o nome do aluno: ')
nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
nota3 = float(input('digite a terceira nota: '))
falta = int(input('digite a quantidade de faltas: '))
media = (nota1+nota2+nota3)/3
print('aluno: ' + aluno)
print('media: ' + str(media))
print('falta(s): ' + str( falta))
