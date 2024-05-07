# estruturas condicionais
nota1= float(input('informe a sua primeira nota (0-100): '))
nota2= float(input('informe a sua segunda nota (0-100): '))
media= (nota1+nota2)/2
if media>=60:
    print(f'você passou com {media}, parabéns.')
else:
    print(f'você não passou.')