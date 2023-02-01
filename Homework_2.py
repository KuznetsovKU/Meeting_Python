# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
#            Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
#            Выведите минимальное количество монет, которые нужно перевернуть
#
#            5 -> 1 0 1 1 0
#            2
#
# coin_amount = int(input('Введите количество монеток: '))
# number_side_counter = 0
# emblem_side_counter = 0
#
# for i in range(coin_amount):
#     current_coin_side = int(input("Введите положение монетки (1 - вверх числом, 0 - вверх гербом): "))
#     if current_coin_side == 1:
#         number_side_counter += 1
#     elif current_coin_side == 0:
#         emblem_side_counter += 1
#     else:
#         break
#
# if number_side_counter + emblem_side_counter != coin_amount:
#     print('При вводе / обработке данных были допущены ошибки. Повторите операцию.')
# else:
#     print(number_side_counter if number_side_counter <= emblem_side_counter else emblem_side_counter)

print()

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
#            Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
#            Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
#
#            4 4 -> 2 2
#            5 6 -> 2 3
#
# summ_numbers = int(input("Введите сумму загаданных чисел: "))
# mult_numbers = int(input("Введите произведение загаданных чисел: "))
#
# for i in range(1, mult_numbers):
#     if mult_numbers % i == 0 and mult_numbers // i + i == summ_numbers:
#         print(f'Загаданные числа: {i} и {mult_numbers // i}')
#         break

print()

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
#
#            10 -> 1 2 4 8
#
# n = int(input('Введите число: '))
#
# for i in range(n):
#     if 2 ** i <= n:
#         print(2 ** i, end=' ')

print()

# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
#     Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
#     Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
#     Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое.
#     Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.

watermellon_amount = int(input("Введите количество арбузов: "))
max_weight = 0
min_weight = 30_000
for _ in range(watermellon_amount):
    current_watermellon = int(input("Введите массу арбуза: "))
    if current_watermellon > max_weight:
        max_weight = current_watermellon
    if current_watermellon < min_weight:
        min_weight = current_watermellon
print(f'Арбуз для меня весит {max_weight}, арбуз для тещи весит {min_weight}')