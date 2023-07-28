'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostra uma mensagem dizendo que ele foi multado.
A multa vai R$7,00 por cada Km acima do limite.
'''
velocidade = int(input('Em qual velocidade você estava? '))
if velocidade >80:
    print('Você foi multado por excesso de velocidade que é de 80Km/h, o valor de multa é R${:.2f}.'.format((velocidade - 80) * 7))
else:
    print('Você estava na velocidade recomendada, então não havera multa.')