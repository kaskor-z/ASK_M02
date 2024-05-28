#           ВАРИАНО КОДА 2
#           ( строк кода - 30, итераций - 210))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
namber_of_chek = len(numbers)
y = 0           #    Клличество итераций
for i in range(1, namber_of_chek):
    for j in range(namber_of_chek):
        y += 1
        is_prime = (numbers[j] % numbers[i] == 0) and (numbers[j] != numbers[i])
        if is_prime:
            if (numbers[j] in not_primes):
                continue
            else:
                not_primes .append(numbers[j])
            if numbers[j] in primes:
                primes .remove(numbers[j])
        else:
            if (numbers[j] in primes) or (numbers[j] in not_primes):
                continue
            else:
                primes .append(numbers[j])
    if len(numbers) == (len(primes) + len(not_primes) - 1):
        break
primes .pop(0)

print('\nКлличество итераций : ', y, '\n')

# ВЫВОД Результатов в Консоль

print('Заданное значение списка\n\tnumbers = ', numbers)
print('финальное значение списка primes = ', primes)
print('финальное значение списка not_primes = ', not_primes)
