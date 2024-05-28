#           ВАРИАНО КОДА 1
#           ( строк кода - 25, итераций - 39))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
number_of_chek_1 = len(numbers)
y = 0           #    Клличество итераций
for i in range(1, number_of_chek_1):
    if i == 1:
        j = 1
        is_prime = (numbers[i] % numbers[j] == 0) and (numbers[j] != numbers[i])
    else:
        for j in range(1, i):
            y += 1
            is_prime = (numbers[i] % numbers[j] == 0) and (numbers[j] != numbers[i])
            if is_prime:
                break
    if is_prime:
        not_primes .append(numbers[i])
    else:
        primes .append(numbers[i])

print('\nКлличество итераций : ', y, '\n')

# ВЫВОД Результатов в Консоль

print('Заданное значение списка\n\tnumbers = ', numbers)
print('финальное значение списка primes = ', primes)
print('финальное значение списка not_primes = ', not_primes)
