preco = float(input('digite o preço: '))
desc = float(input('quantos porcentos de desconto?: '))
novopreco = preco - (preco*desc /100)


print('o preço com desconto de {}% é: {} '.format(desc, novopreco))