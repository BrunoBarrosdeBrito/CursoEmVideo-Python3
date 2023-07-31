'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
EX: Ana Maria de Souza
primeiro= Ana
ultimo= Souza
'''
nome = str(input('Digite o seu nome completo: ')).strip()
separar = nome.split()
print('O seu primeiro nome é {}'.format(separar[0]))
print('O seu último nome é {}'.format(separar[len(nome) - 1]))