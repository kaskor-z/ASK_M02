my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print('Analyzed list: ', my_list)
max_index = len(my_list)
i = 0
while i < max_index:
    if int(my_list[i]) >= 0:
        print(my_list[i])
        i += 1
        continue
    else:
        break
print('END - Это окончание Кода\n')
print(f'Конец выполнения программы:\n\t Значение i = {i}'
      f'\tЭлемент останова: {my_list[i-1]} (включительно)')
