'''
crie um programa que leia o nome completo de uma pessoa e mostre:
-o nome com todas as letras maiúsculas.
-o nome com todas as letras minusculas.
-quantas letras ao todo(sem espaços).
-quantas letras te o primeriro nome. '''
print('-----------------------------------------')

nome = input('digite seu nome completo: ')
print("seu nome em maiusculas é: ",nome.upper())
print('seu o nome em munusculas é: ',nome.lower())
print('seu nome tem: ',len(nome))
print('seu primeiro nome é: ',nome[0:6])


print('-----------------------------------------')
