#Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salário, com 15% de aumento.
sal = float(input('Qual e o salário do funcionário? RS:'))
novo = sal + (sal * 15 / 100)
print('Um funcionário que ganhva R${:.2f}, com 15% de aumento, passa a receber R${:.2f}.'.format(sal, novo))