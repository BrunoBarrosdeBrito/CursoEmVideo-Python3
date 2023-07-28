'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O Programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
from random import randint
from time import sleep
pc = randint(0, 5) # Faz o pc esolher em um núemro
print('-=-' * 20)
print('Vou pensar em um número en 0 e 5. Tente acerta o número.')
print('-=-' * 20)
r = int(input('Em qual número eu pensei? ')) # O usúario tenta acertar o número
print('PROCESSANDO...')
sleep(3)
if r == pc:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI!, Eu pensei no número {} e não no {}!'.format(pc, r))

