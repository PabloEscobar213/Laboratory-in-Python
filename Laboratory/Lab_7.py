import math

#Функция площади треугольника
def area(a, b, c):
   
    p = (a + b + c) / 2

    s = math.sqrt(p * (p - a) * (p - b) * (p - c))

    return s


#Замена первого и последнего элемента
def swapFirstLast(arr):

    if len(arr) > 1:
        arr[0], arr[-1] = arr[-1], arr[0]


#Функция сумм
def sumDigits(n):
    s = 0

    while n > 0:
        s += n % 10     
        n //= 10         
    return s


#Произведение элементов массива
def product(arr):
    p = 1  

    for x in arr:
        p *= x
    return p


#Ср. арефметическое 
def average(arr):

    return sum(arr) / len(arr)



print("Введите стороны первого треугольника:")
a1 = float(input("a1 = "))
b1 = float(input("b1 = "))
c1 = float(input("c1 = "))

# Второй треугольник
print("\nВведите стороны второго треугольника:")
a2 = float(input("a2 = "))
b2 = float(input("b2 = "))
c2 = float(input("c2 = "))

# Третий треугольник
print("\nВведите стороны третьего треугольника:")
a3 = float(input("a3 = "))
b3 = float(input("b3 = "))
c3 = float(input("c3 = "))

# Вычисление площадей
s1 = area(a1, b1, c1)
s2 = area(a2, b2, c2)
s3 = area(a3, b3, c3)

print("\nПлощади треугольников:")
print("S1 =", s1)
print("S2 =", s2)
print("S3 =", s3)

if abs(s1 - s2) < 1e-6 and abs(s2 - s3) < 1e-6:
    print("Треугольники равновелики.")
else:
    print("Треугольники НЕ равновелики.")


# Вводим длину массива
m = int(input("Введите длину массива: "))

A = []
print("Введите элементы массива:")

# Заполняем массив — обычный цикл
for i in range(m):
    A.append(int(input()))

print("Исходный массив:", A)

# Происходит вызов процедуры, которая меняет элементы местами
swapFirstLast(A)

print("Преобразованный массив:", A)




