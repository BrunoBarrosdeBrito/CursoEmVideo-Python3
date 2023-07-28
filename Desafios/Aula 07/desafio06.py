#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n1 = int(input('Digite um número: '))
dob = n1 * 2
tri = n1 * 3
qua = n1 ** (1/2)
print('O número {} tem o dobro de {} \nCom um triplo de {} \nCom uma raiz quadrada de {:.3f}'.format(n1, dob, tri, qua))

