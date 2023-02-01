# a = 'hello'
# for i in a:
#     print(i)
#
# for e in range(10):
#     print(e)
#
# for ind in range(len(a)):
#     print(a[ind])

print()

# 9. По данному целому неотрицательному n вычислите значение n!.
#    N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

# n = int(input('Введите целое неотрицательное число: '))
# factorial_n = 1
# while n > 0:
#     factorial_n *= n
#     n -= 1
# print(factorial_n)

print()

# 11. Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A.
#     Если А не является числом Фибоначчи, выведите число -1

# a = int(input('Введите натуральное число (больше 1): '))
#
# fibo_start_counter = 0
# fibo_end_counter = 1
# fibo_position_counter = 2
# while fibo_end_counter < a:
#     fibo_curent_num = fibo_start_counter +fibo_end_counter
#     fibo_start_counter = fibo_end_counter
#     fibo_end_counter = fibo_curent_num
#     fibo_position_counter += 1
# if fibo_end_counter == a:
#     print(f'Число {a} является {fibo_position_counter} по счету числом Фибоначчи')
# else:
#     print(-1)

print()

# 13. Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой.
#     Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы.
#     Их интересует, сколько дней длилась самая длинная оттепель.
#     Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия.
#     Напишите программу, помогающую синоптикам в работе.
#
#     Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.
#     Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50
#
overwatch_days = int(input('Введите количество рассматриваемых дней: '))
max_thaw_period = 0
current_thaw_period = 0
for _ in range(overwatch_days):
    temperature = int(input('Введите среднесуточную температуру за день: '))
    if temperature > 0:
        current_thaw_period += 1
    else:
        if current_thaw_period > max_thaw_period:
            max_thaw_period = current_thaw_period
        current_thaw_period = 0
# if current_thaw_period > max_thaw_period:
#     max_thaw_period = current_thaw_period
print(f'Самая длинная оттепель длилась {max_thaw_period} дней')

print()

# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
#     Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
#     Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
#     Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое.
#     Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.

# watermellon_amount = int(input("Введите количество арбузов: "))
# max_weight = 0
# min_weight = 30_000
# for _ in range(watermellon_amount):
#     current_watermellon = int(input("Введите массу арбуза: "))
#     if current_watermellon > max_weight:
#         max_weight = current_watermellon
#     if current_watermellon < min_weight:
#         min_weight = current_watermellon
# print(f'Арбуз для меня весит {max_weight}, арбуз для тещи весит {min_weight}')