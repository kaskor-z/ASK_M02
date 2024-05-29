def get_matrix(n, m, value):
    matrix = []
    if value <= 0 or (n <= 0) or (m <=0):
        return matrix
    internal_line = []
    for i in range(n):
        internal_line.clear()
        for j in range(m):
            internal_line.append(value)
        matrix.append(internal_line)
    return matrix


x = int(input('введите колличество строк в матрице = '))
y = int(input('введите колличество столбцов в матрице = '))
z = int(input('введите значение элемента в матрице = '))
new_matrix = get_matrix(x, y, z)
print("\nРезультат заполнения Матрицы = ", new_matrix)
