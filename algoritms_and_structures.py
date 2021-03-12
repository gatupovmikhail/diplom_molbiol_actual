import random

def generate(answer=18, max_len=5):
    k = answer
    test = []
    s = max_len
    a = 0
    b = 0
    for i in range(k):
        a = random.randint(b, b + s // 2)
        b = random.randint(a + 3, a + s + 1)
        test.append((a, b))

    for i in range(1, k - 1):
        for j in range(0, k - i):
            a = random.randint(test[j][0] + 1, test[j][1] - 1)
            b = random.randint(test[j + i][0] + 1, test[j + i][1] - 1)
            test.append((a, b))
    random.shuffle(test)
    return test

for n in [5,8,12,15,20]: #  n - ожидаемое количество уроков
    test = generate(answer=n)  # тестовые данные
    result = [] # здесь будет составленное расписание
    b0 = -1  # конец предыдущего урока.
    while not (len(test) == 0):
        # поиск урока, оканчивающегося раньше всех
        b_min = 10**6 # самое маленькое время окончания урока
        index_b_min = -1
        for i in range(len(test)):
            a = test[i][0]
            b = test[i][1]
            if a >= b0 and b < b_min: # ищем урок, который следует за предыдущим уроком, но при этом
                # оно  оканчивается раньше всех остальных
                index_b_min = i
                b_min = b
        b0 = b_min # меняем время предыдущего урока

        if not(index_b_min == -1):
            result.append(test[index_b_min]) # добавляем урок в расписание
            test.pop(index_b_min) # удаляем выбранный урок из списка всех остальных
        else:
            break # если не нашли урока, который следует за предыдущим,
            # то выхоим из цикла и заканчиваем составление расписания.
    print('Расписание')
    print(result) # составленное расписание
    print('Количество уроков')
    print(len(result)) # количество уроков
    print('Ожидаемое количество уроков')
    print(n)
    print()

