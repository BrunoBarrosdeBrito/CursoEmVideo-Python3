'''
Faça um programa que leia na frase pelo teclado e mostre:
->Quantas vezes aparece a letra "A".
->Em que posição ela aparece a primeira vez.
->Em que posição ela aparece a úlltima vez.
'''
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" apareceu {} vezes.'.format(frase.count('A')))
print('A primeira letra "A" aparaceu na posição {}'.format(frase.find('A') + 1))
print('A ultima letra "A" apareceu na posição {}'.format(frase.rfind('A') + 1))