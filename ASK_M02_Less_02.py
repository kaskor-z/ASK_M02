print('     БЛОК № 1')
x = 38
print('дратуйте!')
if x < 0 :
    print('Меньше нуля.')
print('дотвидания!')

print('     БЛОК № 2')
# пример
a, b = 10, 5
if a > b:
    print('a > b')
if a > b and a > 0:
    print('успех')
if (a > b) and (a > 0 or b < 1000):
    print('успех')
if 5 < b and b < 10:
    print('успех')

print('     БЛОК № 3')
# можно сравнивать - числап, строки, списки, вообще -...
if '34' > '123':
    print('успех')
if '123' > '12':
    print('успех')
if [1, 2] > [1, 1]:
    print('успех')

print('     БЛОК № 4')
# что нельзя сравнивать - разные типы
if '6' > 5:
    print('успех')
if [5, 6] > 5:
    print('успех')

print('     БЛОК № 5')
# но
if '6' != 5:
    print('успех')