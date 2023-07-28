#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros.
n1 = float(input('Digite aqui a quantidade de metros: '))
cm = n1 * 100
mm = n1 * 1000
print('A quantidade de metros foi {} \nEm cm é {:.0f} \nEm mm é {:.0f}'.format(n1, cm, mm))