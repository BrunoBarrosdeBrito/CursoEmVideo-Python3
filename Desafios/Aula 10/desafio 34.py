'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
Para salário superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais o aumento é de 15%.
'''
salário = float(input('Digite o salário do funcionario: R$'))
if salário <=1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))