def o_x_game():
    print('Приветствую тебя в игре Крестики-нолики!')
    play_area = [[' ', '1', '2', '3'],
                 ['1', '-', '-', '-'],
                 ['2', '-', '-', '-'],
                 ['3', '-', '-', '-']
                 ]

    win_init = [[[1,1], [1,2], [1,3]], [[1,1], [2,2], [3,3]], [[1,1], [2,1], [3,1]],
                [[1,2], [2,2], [3,2]], [[1,3], [2,3], [3,3]], [[1,3], [2,2], [3,1]],
                [[2,1], [2,2], [2,3]], [[3,1], [3,2], [3,3]]]

    for i in play_area:
        print(*i)


    def o_playing():
        print('Ход ноликов:')
        print('Впиши поле, которое хочешь занять. Сначала введи строку, потом столбик')
        while True:
            try:
                stroka = int(input("Введите число: "))
                stolb = int(input("Введите число: "))
                break
            except ValueError:
                print("Некорректный ввод. Введите число.")
        while stroka not in range(1, 4) and stolb not in range(1, 4):
            print('Сожалеем, Вы ввели некорректную клетку')
            while True:
                try:
                    stroka = int(input("Введите число: "))
                    stolb = int(input("Введите число: "))
                    break
                except ValueError:
                    print("Некорректный ввод. Введите число.")
        if play_area[stroka][stolb] == '-':
            play_area[stroka][stolb] = 'O'
        else:
            print("Поле уже занято, выбери другое")


    def x_playing():
        print('Ход крестиков:')
        print('Впиши поле, которое хочешь занять. Сначала введи строку, потом столбик')
        while True:
            try:
                stroka = int(input("Введите число: "))
                stolb = int(input("Введите число: "))
                break
            except ValueError:
                print("Некорректный ввод. Введите число.")
        while stroka not in range(1, 4) and stolb not in range(1, 4):
            print('Сожалеем, Вы ввели некорректную клетку')
            while True:
                try:
                    stroka = int(input("Введите число: "))
                    stolb = int(input("Введите число: "))
                    break
                except ValueError:
                    print("Некорректный ввод. Введите число.")
        if play_area[stroka][stolb] == '-':
            play_area[stroka][stolb] = 'X'
        else:
            print("Поле уже занято, выбери другое")

    def check_winner():
        for i in win_init:
            a = i[0]
            b = i[1]
            c = i[2]
            if play_area[a[0]][a[1]] == play_area[b[0]][b[1]] and play_area[a[0]][a[1]] == play_area[c[0]][c[1]] and play_area[a[0]][a[1]] != '-':
                print("Победитель:", play_area[a[0]][a[1]])
                return True

        if '-' not in play_area[1] and '-' not in play_area[2] and '-' not in play_area[3]:
            print('Игра завершена. Победителя нет.')
            return True

        return False

    control_num = 0
    while control_num == 0:
        o_playing()
        for i in play_area:
            print(*i)
        if check_winner() is True:
            break

        x_playing()
        for i in play_area:
            print(*i)
        if check_winner() is True:
            break

o_x_game()