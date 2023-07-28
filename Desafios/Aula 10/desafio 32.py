'''
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
'''
ano = int(input('Que ano quer aalisar? Coloque 0 analise o ano atual: '))
if ano % 4 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não e BISSEXTO'.format(ano))