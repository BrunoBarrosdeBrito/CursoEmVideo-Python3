'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
'''
km = int(input('Qual e a distancia da viagem? '))
if km <=200:
    print('O preço da passagem é R${:.2f}'.format(km * 0.50))
else:
    print('O preço da passagem é R${:.2f}'.format(km * 0.45))
