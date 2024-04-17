import math
c_o = float(input('qual valor do cateto oposto? '))
c_a = float(input('qual valor do cateto adjacente? '))
res = math.hypot (c_o,c_a) 
print('o valor da hypotenusa é {:.2f}'.format(res))