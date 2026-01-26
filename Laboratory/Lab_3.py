#Lаны три целых числа. Выбрать из них те, которые принадлежат интервалу [1,3]. 

x = 1
y = 3
c = 5

num = [x,y,c]

result = [i for i in num if 1 <= i <= 3]

print(result)