#           ВАРИАНО КОДА 3
#       Альтернативное решение - по Алгоритм "Решето Эратосфена"
#       с внутренним циклом While ( строк кода - 23, итераций - 15))

from math import sqrt

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
primes = numbers.copy()  # Копируем значение элементов из строки (numbers) в строку primes
primes.pop(0)  # удаляем значение 1 (которое не относится к простым числам)
namber_primis = int(sqrt(len(numbers)))  # в соответствии с Алгоритмом, колличество делителей
#                                       из последовательности простых чисел определяется как
#                                       (end_range) <= корню кадратному из (n),
#                                       где n = заначение последнего элемента списка
y = 0  # Клличество итераций
for i in range(namber_primis - 1):
    divisor = primes[i]  # присвоение текущего значения делителя
    range_j = len(primes)
    j = 0
    while j <= range_j:
        y += 1
        if (primes[j] % divisor == 0) and (primes[j] != divisor):  # проверка деления
            #                                                        на текущий делитель
            not_primes.append(primes.pop(j))  # перенос составных чисел из списка (primes)
            #                                   в список (not_primes)
        j += 1
        range_j = len(primes) - 1

print('\nКлличество итераций : ', y, '\n')

# ВЫВОД Результатов в Консоль

print('Заданное значение списка\n\tnumbers = ', numbers)
print('финальное значение списка primes = ', primes)
print('финальное значение списка not_primes = ', not_primes)
