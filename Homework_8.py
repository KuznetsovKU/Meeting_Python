# 1. Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно
#    последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число).
#    Протестируем функцию на файле «article.txt» со следующим содержимым:
#       Вечерело
#       Жужжали мухи
#       Светил фонарик
#       Кипела вода в чайнике
#       Венера зажглась на небе
#       Деревья шумели
#       Тучи разошлись
#       Листва зеленела

# def read_last(lines, file):
#     if lines > 0:
#         with open(file, 'r', encoding='utf-8') as file_1:
#             for line in file_1.readlines()[-lines:]:
#                 print(line.strip('\n'))
#     else:
#         print("Проверьте количество возвращаемых строк!")
#
#
# read_last(3, 'article.txt')
print()

# 2. Документ «article.txt» содержит следующий текст:
#       Вечерело
#       Жужжали мухи
#       Светил фонарик
#       Кипела вода в чайнике
#       Венера зажглась на небе
#       Деревья шумели
#       Тучи разошлись
#       Листва зеленела
#
#     Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину
#     (или список слов, если таковых несколько).

#
# def longest_words(file):
#     with open(file, 'r', encoding='utf-8') as file_2:
#         data = file_2.read().split()
#         max_length = 0
#         for word in data:
#             if len(word) > max_length:
#                 max_length = len(word)
#         # max_length = len(max(data, key=len))
#         result = [i for i in data if len(i) == max_length]
#         print(f'Самые длинные слова (или одно слово) в файле: {result}')
#
#
# longest_words('article.txt')

print()

# 3. Классическая задача про бассейн, который заполняется через 3 трубы, слишком проста. У нас труб будет больше.
#    Бассейн можно заполнить из N труб. В файле pipes.txt записаны времена заполнения всего бассейна только одной
#    данной работающей трубой (в часах). Затем после пустой строки перечислены трубы, которые будут заполнять бассейн.
#    Сколько минут на это потребуется?
#    Номер трубы соответствует номеру строки, в которой записана ее производительность.
#    Результат запишите в файл time.txt
#   Пример
#   Ввод
#    1
#    2
#    3
#    (пустая строка)
#    1 2 3
#   Вывод: 32.72727272727273


# def fill_pipes_productivity(pipes_amount=3):
#     with open('pipes.txt', 'w', encoding='utf-8') as pipes_prod:
#         for _ in range(pipes_amount):
#             pipes_prod.write(input('Введите производительность трубы в часах: ') + '\n')

def fill_pipes_productivity():
    with open('pipes.txt', 'w', encoding='utf-8') as pipes_prod:
        while True:
            current_productivity = input('Введите производительность трубы в часах: ')
            if not current_productivity:
                break
            pipes_prod.write(current_productivity + '\n')


def choose_pipes(data):
    with open(data, 'r', encoding='utf-8') as pipes:
        pipes_amount = sum([1 for _ in pipes.readlines()])
        print(f'Введите через "пробел" порядковые номера труб (от 1 до {pipes_amount}) для расчета: ')
        chosen_pipes = [int(i) for i in input().split()]
        return chosen_pipes


def count_time(data, workers):
    with open(data, 'r', encoding='utf-8') as times_list:
        data_list = [int(i) for i in times_list.read().splitlines()]
        speed = sum([1 / data_list[i - 1] for i in workers])
        time = 60 / speed
        with open('time.txt', 'w', encoding='utf-8') as result:
            result.write(f'Бассейн заполнится за {str(time)} минут')


# fill_pipes_productivity()
count_time('pipes.txt', choose_pipes('pipes.txt'))
