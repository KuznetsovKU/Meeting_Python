# Задача №25. Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
#             Количество повторов добавляется к символам с помощью постфикса формата _n.
#             Input: a a a b c a a d c d d
#             Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
#             Для решения данной задачи используйте функцию .split()

# input_string = 'a a a b c a a d c d d'
# elements_list = input_string.split()
# elements_dict = {}
# output_string = ''
# output_list = []
# # Формирование словаря без спец.методов:
# # unique_elements = set(elements_list)
# # for element in unique_elements:
# #     counter = 0
# #     for i in elements_list:
# #         if i == element:
# #             counter += 1
# #     elements_dict[element] = counter
#
# # Формирование словаря со спец.методом:
#
# # for element in elements_list:
# #     elements_dict[element] = elements_dict.get(element, 0) + 1
# #     # сборка строки
# # #     if elements_dict.get(element) > 1:
# # #         output_string += f'{element}_{str(elements_dict[element])} '
# # #     else:
# # #         output_string += f'{element} '
# # # print(output_string[:-1])
# #
# #     # сборка списком
# #     if elements_dict.get(element) > 1:
# #         output_list.append(element + '_' + str(elements_dict.get(element) - 2))
# #     else:
# #         output_list.append(element)
# # print(' '.join(output_list))
#
# # string = input_string.split()
# # for i in range(len(string)):  # не оптимальное решение при сильном увеличении количества элементов
# #     counter = 0
# #     for j in range(i + 1, len(string)):
# #         if string[i] == string[j]:
# #             counter += 1
# #             string[j] = f'{string[j]}_{counter}'
# # print(*string)

print()

# Задача №27. Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
#             слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
#        Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea
#             shells on the sea shore I'm sure that the shells are sea shore shells
#       Output: 13
#
# input_text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# words_list = []
# word = ''
# for i in range(len(input_text)):
#     if input_text[i].isalpha() or input_text[i] == "'":
#         word += input_text[i]
#     else:
#         words_list.append(word.upper())
#         word = ''
#
# unique_word_counter = len(set(words_list))
# print(unique_word_counter)
# print(set(words_list))

print()

# Задача Extra: Дана последовательность чисел. Необходимо получить список уникальных (не повторяющихся) элементов заданной последовательности.
#         Input: [1, 2, 3, 5, 1, 5, 3, 10]
#        Output: [2, 10]

input_array = [1, 2, 3, 5, 1, 5, 3, 10]
output_array = []
# numbers_dict = {}
# for number in input_array:
#     numbers_dict[number] = numbers_dict.get(number, 0) + 1
# for key in numbers_dict:
#     if numbers_dict[key] == 1:
#         output_array.append(key)
for number in input_array:
    if input_array.count(number) == 1:
        output_array.append(number)
print(output_array)