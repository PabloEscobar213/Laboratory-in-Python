#Практическая №2. Написать прогрраму, которая будет вычислять заданное арифметическое выражение при заданных переменных.

import math

x = int(input("Введите переменную X: "))
t = int(input("Введите переменную t: "))

z = ((9*math.pi*t+10*math.cos(x))/(math.sqrt(t)-math.fabs(math.sin(t))))*math.pow(math.e,x)

print('z = {0:.2f}'.format(z))