# Задача №31. Последовательностью Фибоначчи называется последовательность чисел a0 , a1 , ..., an , ..., где
#             a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
#             Требуется найти N-е число Фибоначчи
#       Input: 7
#       Output: 21
#       Задание необходимо решать через рекурсию

# requested_num = int(input('Введите порядковый номер числа в последовательности Фибоначчи: '))
#
#
# def find_fibo(number):
#     if number == 0 or number == 1:
#         return number
#     else:
#         return find_fibo(number - 1) + find_fibo(number - 2)
#
#
# def fill_fibo_array(number):
#     output_array = []
#     for i in range(number + 1):  # т.к. считаем, что 0 - это НУЛЕВОЙ элемент
#         output_array.append(find_fibo(i))
#     return output_array
#
#
# fibo_array = fill_fibo_array(requested_num)
# print(*fibo_array)
# print(f'Числом с порядковым номером {requested_num} в последовательности Фибоначчи является число {find_fibo(requested_num)}')

print()


# Задача №33. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
#             Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
#       Input: 5 -> 1 3 3 3 4
#       Output: 1 3 3 3 1

# points_amount = int(input('Введите количество оценок в журнале: '))
#
#
# def fill_points_array(count):
#     output_array = []
#     for i in range(count):
#         output_array.append(int(input('Введите оценку ученика: ')))
#     return output_array
#
#
# def change_points(input_array):
#     max_score = max(input_array)
#     min_score = min(input_array)
#     if max_score != min_score:
#         for i in range(len(input_array)):
#             if input_array[i] == max_score:
#                 input_array[i] = min_score
#     return input_array
#
#
# points_array = fill_points_array(points_amount)
# print(points_array)
# print(change_points(points_array))


print()


# Задача №35. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
#             Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
#        Input: 5
#        Output: yes
#
# def is_simple(number):
#     flag = True
#     for i in range(2, number // 2 + 1):
#         if number % i == 0:
#             flag = False
#             break
#     print(f"Число {number} является простым" if flag else f"Число {number} не является простым")
#
#
# is_simple(int(input('Введите число: ')))

print()

# Задача №37. Дано натуральное число N и последовательность из N элементов.
#             Требуется вывести эту последовательность в обратном порядке.
#             Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
#       Input: 2 -> 3 4
#       Output: 4 3

amount = int(input('Введите количество элементов: '))


def fill_sequence(elements_amount):
    line = ''
    if elements_amount == 1:
        line += input('Введите очередной элемент последовательности: ')
        return line
    else:
        return fill_sequence(elements_amount - 1) + input('Введите очередной элемент последовательности: ')


def reverse_line(input_line):
    output_line = ''
    if len(input_line) == 1:
        output_line += input_line[-1]
        return output_line
    else:
        return input_line[-1] + reverse_line(input_line[:-1])


sequence_line = fill_sequence(amount)
sequence_line_revere = reverse_line(sequence_line)
print(' '.join(sequence_line_revere))
