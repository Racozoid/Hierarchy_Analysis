import math
print('''В программе вам необходимо ввести сначала количество критериев для сравнения (целое, положительное число)
Далее вам необходимо ввести весовые коэффициенты следующим образом:
1 -- равная важность
3 -- умеренное превосходство одного над другим
5 -- существенное превосходство одного над другим
7 -- значительное превосходство одного над другим
9 -- очень сильное превосходство одного над другим
2, 4, 6, 8 -- соответствующие промежуточные значения
Если критерий наоборот не превосходит другой, то введите обратное значение
(Обратное значение = 1/n, где n -- соответствующий весовой коэффициент, десятичные числа вводятся через точку!)

Предупреждение! Если вы введете коэффициенты намного превосходящие предложенные, 
то один критерий перевесит остальные.''')

while True:
    # Ввод количества критериев и проверка на правильность введения
    try:
        n = abs(int(input('\nВведите количество критериев (целое, положительное число): ')))
    except ValueError:
        print('Введено некорректное значение количества критериев.\nПопробуйте снова\n')
        continue
    if n == 0:
        print('Введен ноль.\nПопробуйте снова.\n')
        continue
    elif n == 1:
        print('Сравнение одного критерия невозможно(но коэффициент у него будет равен 1)')
        break

    # Создание таблицы попарного сравнения состоящей из единиц
    table = [[1.0] * n for i in range(n)]

    # Заполнение таблицы за исключением главной диагонали
    try:
        for i in range(n - 1):
            for j in range(i + 1, n):
                table[i][j] = float(input(f'Насколько параметр {i+1} важнее параметра {j+1}: '))
                table[j][i] = 1 / table[i][j]
                # Округление до двух знаков после запятой(или до 0, если число больше 1)
                if table[i][j] > 1:
                    table[i][j] = float(math.floor(table[i][j]))
                else:
                    table[i][j] = float(math.floor(table[i][j] * 100)/100)
                if table[j][i] > 1:
                    table[j][i] = float(math.floor(table[j][i]))
                else:
                    table[j][i] = float(math.floor(table[j][i] * 100)/100)
    except ValueError:
        print('Введено некорректное значение.\nПопробуйте снова.\n')
        continue
    except ZeroDivisionError:
        print('Введен ноль.\nПопробуйте снова.\n')
        continue

    # Создание и заполнение списка сумм строк
    list_of_sum = list()

    for i in range(n):
        s = 0
        for j in range(n):
            s += table[i][j]
        list_of_sum.append(s)

    # Создание и заполнение списка весовых коэффициентов
    list_of_alpha = list()

    for i in range(n):
        list_of_alpha.append(math.floor((list_of_sum[i]/sum(list_of_sum)) * 100) / 100)

    # Доведение суммы до 1
    while sum(list_of_alpha) > 1:
        for i in range(n):
            if list_of_alpha[i] == min(list_of_alpha):
                list_of_alpha[i] -= 0.01
    while sum(list_of_alpha) < 1:
        for i in range(n):
            if list_of_alpha[i] == max(list_of_alpha):
                list_of_alpha[i] += 0.01

    # Вывод таблицы
    print('\nТаблица попарного сравнения')
    for i in range(n):
        for j in range(n):
            print(table[i][j], end=' \t')
        print('')

    # Вывод коэффициентов
    print('\nКоэффициенты')
    for i in range(n):
        print(f'Коэффициент критерия {i+1}: {round(list_of_alpha[i], 2)}')
    break
input('Press ENTER to exit')
