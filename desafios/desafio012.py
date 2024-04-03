preco = float(input('digite o preço: '))
desc = float(input('quantos porcentos de desconto?: '))
v_desc = desc /100
v_total = preco - v_desc

print('o preço com desconto de {}% é: {} '.format(desc, v_total))