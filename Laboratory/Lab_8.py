def input_matrix(n, msg="Введите матрицу:"):
    print(msg)
    A = []
    for i in range(n):
        
        row = list(map(float, input().split()))
        
        if len(row) != n:
            print("Ошибка: в строке должно быть", n, "элементов.")
            exit()
        A.append(row)
    return A


def task1(A, k):
    count = 0
    max_elem = None

    # Проходим по всей матрице 
    for row in A:
        for elem in row:
            if elem % k == 0:
                count += 1
                if max_elem is None or elem > max_elem:
                    max_elem = elem

    return count, max_elem


def task2(A):
    n = len(A)

    # Ищем максимальный по модулю элемент
    max_val = None
    max_i = 0
    max_j = 0

    for i in range(n):
        for j in range(n):
            # Происходит сравнение по модулю
            if max_val is None or abs(A[i][j]) > abs(max_val):
                max_val = A[i][j]
                max_i = i
                max_j = j

    new_matrix = []

    for i in range(n):
        if i == max_i:
            continue  # пропускаем строку
        row = []
        for j in range(n):
            if j == max_j:
                continue  # пропускаем столбец
            row.append(A[i][j])
        new_matrix.append(row)

    return max_val, new_matrix


print("Лабораторная работа №8 — Работа с двумерными массивами\n")

# Вводим размер квадратной матрицы
n = int(input("Введите порядок матрицы n: "))

# Вводим матрицу для обоих заданий
A = input_matrix(n, "Введите квадратную матрицу:")

print("\nИсходная матрица:")
for row in A:
    print(*row)

print("\n=== Задание 1 ===")
k = int(input("Введите число k: "))

count, max_elem = task1(A, k)

print("Количество элементов, кратных", k, ":", count)
if max_elem is None:
    print("Элементов, кратных k, нет.")
else:
    print("Наибольший из кратных k элементов:", max_elem)

print("\n=== Задание 2 ===")

max_val, reduced_matrix = task2(A)

print("Максимальный по модулю элемент:", max_val)
print("Матрица после удаления строки и столбца:")

for row in reduced_matrix:
    print(*row)
