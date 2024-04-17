from math import radians, sin, cos, tan
num = float(input('digite um angulo:  '))
s = sin(radians(num))
c = cos(radians(num))
t = tan(radians(num)) 
print('o valor sin {:.2}, valor cos {:.2}, valor tan {:.2}'.format(s, c, t))