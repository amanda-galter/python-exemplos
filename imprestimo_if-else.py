#impréstimo questionaroa if-else
print(f'programa de emprestimo\n'
      f'responda:: (0=não ou 1=sim)')
nome_neg=int(input('possui nome negativado?'))
if nome_neg == 1:
    print('não será possível realizar o impréstimo.')
else:
    carteira_assinada=int(input('possui carteira assinada?'))
    if carteira_assinada==0:
        print('não será possível realizar o impréstimo.')
    else:
        casa_propria=int(input('possui casa propria?'))
        if casa_propria==1:
            print('conceder imprestimo.')
        else:
            print('não será possível realizar o impréstimo.')