def def_divisors(number, list_):
    divisors = []
    i = 0
    while (number != list_[i - 1]) or ((number == list_[-1]) and ((len(list_) - i) != 0)):
        if number % list_[i] == 0:
            divisors.append(list_[i])
        i += 1
    return divisors


def parsing_divisors(divisors):
    key = ''
    for i in range(len(divisors)):
        k = int(divisors[i] / 2)
        if divisors[i] % 2 == 0:
            k -= 1
        n1 = 0
        n2 = divisors[i]
        for j in range(k):
            n2 -= 1
            n2_str = str(n2)
            n1 += 1
            n1_str = str(n1)
            key += (n1_str + n2_str)
    return key


list_n = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# print('\nВсе пароли для чисел от 3 до 20 (для сверки):\n')
n = int(input('\nВведите число для определения ключа : '))
# i = 0
# while i != (len(list_n)):
#     n = list_n[i]
divisor_ = def_divisors(n, list_n)
keyword_ = parsing_divisors(divisor_)
print('\nКодовая последовательнсть ключа для введённого числа = ',  n, '\n\n\t', keyword_)
    # print('\t', list_n[i], '. -\t', keyword_)
    # i += 1
