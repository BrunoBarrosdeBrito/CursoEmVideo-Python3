#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
prod = float(input('Qual é o preço do produto? R$'))
novo = prod - (prod * 5 / 100) 
print('O produto que custava {:.2f}, na promoção com o desconto de 5% vai cistar {:.2f}.'.format(prod, novo))