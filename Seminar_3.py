# 17. Дан список чисел. Определите, сколько в нем встречается различных чисел
#
# numbers = [1, 2, 2, 24, 5, 5, 8, 8, 9]
# unique_numbers = set(numbers)
# print(f'Количество уникальных чисел в списке: {len(unique_numbers)}')

print()

# 19. Дана последовательность из N целых чисел и число K.
#     Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
#     Input: [1, 2, 3, 4, 5] k = 3
#     Output: [4, 5, 1, 2, 3]
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# k = int(input('Введите параметр сдвига: '))
#
# current_move_steps = k % len(numbers)
# output_list = []
# for i in range(len(numbers)):
#     output_list.append(numbers[i + current_move_steps - len(numbers)])
# print(output_list)

print()

# 21. Напишите программу для печати всех уникальных значений в словаре.
#     Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
#     Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
#     Примечание: Список словарей задан изначально. Пользователь его не вводит

# list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII ":"S007"}]
# set_1 = set()
# for i in list_1:
#     for j in i:
#         set_1.add(i[j])
# print(set_1)

print()

# 23. Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива,
#     больших предыдущего (элемента с предыдущим номером)
#     Input: [0, -1, 5, 2, 3]
#     Output: 2 (-1 < 5, 2 < 3)
#
# input_array = [0, -1, 5, 2, 3]
# counter = 0
#
# for i in range(1, len(input_array)):
#     if input_array[i] > input_array[i - 1]:
#         counter += 1
#
# print(counter)