# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на
# указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import random
amount = int(input('Введите число: '))
my_list = [random.randint(-amount, amount) for i in range(amount)]

with open('some_file.txt', 'w', encoding='utf-8') as file_1:
    for i in range(amount - 1):
        file_1.write(str(random.randint(0, amount - 1)) + '\n')

with open('some_file.txt', 'r', encoding='utf-8') as file_1:
    mult = 1
    for i in file_1.read().splitlines():
        mult *= my_list[int(i)]

print(my_list)
print(mult)