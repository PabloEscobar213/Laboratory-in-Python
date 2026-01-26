n = int(input("Введите длину массива: "))

A = [int(input(f"A[{i}] = ")) for i in range(n)]

print("Исходный массив:", A)

for i in range(n):
    if A[i] < 0:
        A[i] = -A[i]

print("Преобразованный массив:", A)
