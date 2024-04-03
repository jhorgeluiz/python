valorsalario = float(input('Digite o valor do salario: '))
porc = float(input('digite o valor da porcentagem: '))
diaria = valorsalario /30
porc = porc/100
acre = diaria*porc
tpor = acre*30
novosal = valorsalario + tpor

print('O valor do salario com acrescimo de 15% é: ',novosal)