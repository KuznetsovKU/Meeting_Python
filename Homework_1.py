# Задача 2: Найдите сумму цифр трехзначного числа.
#           123 -> 6 (1 + 2 + 3)
#           100 -> 1 (1 + 0 + 0)

# num = input('Введите трехзначное число: ')
#
# condition_check = True
# if num[0] == '-':
#     num = num[1:]
# if len(num) != 3:
#     condition_check = False
# if not num.isdigit():
#     condition_check = False
#
# if condition_check:
#     summ_digits_str = int(num[0]) + int(num[1]) + int(num[2])
#     print(f'Сумма цифр по срезам строки равна: {summ_digits_str}')
#
#     number = int(num)
#     summ_digits = 0
#     while number // 10 != 0:
#         summ_digits += number % 10
#         number = number // 10
#     summ_digits += number
#     print(f'Сумма цифр по int равна: {summ_digits}')
# else:
#     print('Введите корректные данные!')

print()

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
#           Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
#           а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#           6 -> 1  4  1
#           24 -> 4  16  4
#           60 -> 10  40  10

# crane_amount = int(input('Введите общее количество журавликов: '))
# kate_result = crane_amount // 3 * 2
# piter_result = (crane_amount - kate_result) // 2
# serg_result = piter_result
# print(piter_result, kate_result, serg_result)

print()

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
#           Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
#           Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
#           385916 -> yes
#           123456 -> no

# ticket_num = input('Введите номер билета: ')
#
# def count_summ_digits(number):
#     summ_digits = 0
#     while number // 10 != 0:
#         summ_digits +=number % 10
#         number //= 10
#     summ_digits += number
#     return summ_digits
#
# def check_conditions(number):
#     condition = True
#     if not number.isdigit():
#         condition = False
#     if len(number) != 6:
#         condition = False
#     return condition
#
# if check_conditions(ticket_num):
#     first_part_summ = count_summ_digits(int(ticket_num[:3]))
#     second_part_summ = count_summ_digits(int(ticket_num[3:]))
#     print('YES' if first_part_summ == second_part_summ else 'NO')

print()

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками
#           (то есть разломить шоколадку на два прямоугольника).
#           3 2 4 -> yes
#           3 2 1 -> no

choco_length = int(input('Введите длину шоколадки: '))
choco_width = int(input('Введите ширину шоколадки: '))
need_parts = int(input('Укажите, сколько долек нужно отломить: '))

if need_parts <= choco_width * choco_length and (need_parts % choco_length == 0 or need_parts % choco_width == 0):
    print('YES')
else:
    print('NO')
