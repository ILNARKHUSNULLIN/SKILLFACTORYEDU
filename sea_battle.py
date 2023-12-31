import random

class Dot:
    def __init__(self):
        self.board = [[' ', 1, 2, 3, 4, 5, 6],
             [1, '0', '0', '0', '0', '0', '0'],
             [2, '0', '0', '0', '0', '0', '0'],
             [3, '0', '0', '0', '0', '0', '0'],
             [4, '0', '0', '0', '0', '0', '0'],
             [5, '0', '0', '0', '0', '0', '0'],
             [6, '0', '0', '0', '0', '0', '0']]

    def __str__(self):
        for i in self.board:
            print(*i, sep=' | ')
        return ' '

    def board_returner(self):
        return [i for i in self.board]

class Ship:
    def __init__(self, ship_len, ship_head_coordinate, horizontally, ship_lifes):
        self.ship_len = ship_len
        self.ship_head_coordinate = ship_head_coordinate
        self.horizontally = horizontally
        self.ship_lifes = ship_lifes

    def add_to_board(self):
        return [self.ship_head_coordinate, self.horizontally]

class Board:
    def __init__(self, player_dot, ships_list, player, ships_status):
        self.player_dot = player_dot
        self.ships_list = ships_list
        self.player = player
        self.ships_status = ships_status

    def add_ship(self, ship_len): #добавляет корабль
        print('обратите внимание, что корабли не должны граничить')
        try:
            ship_head_coordinate = int(input('Введите точку, где будет расположен нос корабля, например, 11:'))
        except ValueError:
            print('Вы ввели что-то не то! Попробуйте еще раз')
            self.add_ship(ship_len)
        if ship_head_coordinate not in [11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26, 31, 32, 33, 34, 35, 36, 41, 42, 43, 44, 45, 46, 51, 52, 53, 54, 55, 56, 61, 62, 63, 64, 65, 66]:
            print('Введите координату доски, которая есть на игровом поле!')
            self.add_ship(ship_len)
        
        while True:
            horizontally = input('Хотите разместить корабль горизонтально? Если да, пишите True, если нет, то False:')

            if horizontally == 'True':
                horizontally = True
                break
            elif horizontally == 'False':
                horizontally = False
                break
            else:
                print("Вы ввели что-то не так... Введите еще раз")
        ship_lifes = ship_len

        return [ship_len, ship_head_coordinate, horizontally, ship_lifes]

    def win_check(self):
        opp_lifes = 0
        if self.player.name() == 'Игрок':
            for i in self.player.opp_gm_board.board:
                for j in i:
                    if j == '■':
                        opp_lifes += 1
                    else:
                        continue
        else:
            for i in Gm.user_board.board:
                for j in i:
                    if j == '■':
                        opp_lifes += 1
                    else:
                        continue
        return opp_lifes
    
    def shot(self): #делает выстрел
        crd = self.player.ask()
        print(f'{self.player.name()} стреляет в координату:', crd)
        if self.player.name() == 'Игрок':
            if self.player.opp_gm_board.board[crd[0]][crd[1]] == '0' or self.player.opp_gm_board.board[crd[0]][crd[1]] == 'O':
                print('Промах!')
                self.player.opp_gm_board.board[crd[0]][crd[1]] = '-'
                self.player.opp_board.board[crd[0]][crd[1]] = '-'
                return False
            elif self.player.opp_gm_board.board[crd[0]][crd[1]] == '■':
                print('Попал!')
                self.player.opp_gm_board.board[crd[0]][crd[1]] = 'X'
                self.player.opp_board.board[crd[0]][crd[1]] = 'X'
                try:
                    if self.player.opp_gm_board.board[crd[0] + 1][crd[1]] != '■' and self.player.opp_gm_board.board[crd[0] - 1][crd[1]] != '■' and self.player.opp_gm_board.board[crd[0]][crd[1]+1] != '■' and self.player.opp_gm_board.board[crd[0]][crd[1]-1] != '■':
                        print('Убил!')
                        return True
                except Exception:
                    pass
                else:
                    try:
                        if self.player.opp_gm_board.board[crd[0] - 1][crd[1]] != '■' and self.player.opp_gm_board.board[crd[0]][crd[1] + 1] != '■' and self.player.opp_gm_board.board[crd[0]][crd[1] - 1] != '■':
                            print('Убил!')
                            return True
                    except Exception:
                        pass
                    else:
                        try:
                            if self.player.opp_gm_board.board[crd[0] - 1][crd[1]] != '■' and self.player.opp_gm_board.board[crd[0] + 1][crd[1]] != '■' and self.player.opp_gm_board.board[crd[0]][crd[1] - 1] != '■':
                                print('Убил!')
                                return True
                        except Exception:
                            pass
                        else:
                            if self.player.opp_gm_board.board[crd[0] - 1][crd[1]] != '■' and self.player.opp_gm_board.board[crd[0]][crd[1] - 1] != '■':
                                print('Убил!')
                                return True
                return True
        else:
            if Gm.user_board.board[crd[0]][crd[1]] == '0' or Gm.user_board.board[crd[0]][crd[1]] == 'O':
                print('Промах!')
                Gm.user_board.board[crd[0]][crd[1]] = '-'
                return False
            elif Gm.user_board.board[crd[0]][crd[1]] == '■':
                print('Попал!')
                Gm.user_board.board[crd[0]][crd[1]] = 'X'
                try:
                    if Gm.user_board.board[crd[0] + 1][crd[1]] != '■' and Gm.user_board.board[crd[0] - 1][crd[1]] != '■' and Gm.user_board.board[crd[0]][crd[1] + 1] != '■' and Gm.user_board.board[crd[0]][crd[1] - 1] != '■':
                        print('Убил!')
                        return True
                except Exception:
                    pass
                else:
                    try:
                        if Gm.user_board.board[crd[0] - 1][crd[1]] != '■' and Gm.user_boardd.board[crd[0]][crd[1] + 1] != '■' and Gm.user_boardd.board[crd[0]][crd[1] - 1] != '■':
                            print('Убил!')
                            return True
                    except Exception:
                        pass
                    else:
                        try:
                            if Gm.user_board.board[crd[0] - 1][crd[1]] != '■' and Gm.user_board.board[crd[0] + 1][crd[1]] != '■' and Gm.user_board.board[crd[0]][crd[1] - 1] != '■':
                                print('Убил!')
                                return True
                        except Exception:
                            pass
                        else:
                            if Gm.user_board.board[crd[0] - 1][crd[1]] != '■' and Gm.user_board.board[crd[0]][crd[1] - 1] != '■':
                                print('Убил!')
                                return True
                return True


class Player:
    def __init__(self, my_board, opp_board, opp_gm_board):
        self.my_board = my_board
        self.opp_board = opp_board
        self.opp_gm_board = opp_gm_board


class AI (Player):
    @staticmethod
    def name():
        return 'Компьютер'
    def ask(self):
        while True:
            x = random.randint(1, 6)
            y = random.randint(1, 6)
            if (Gm.user_board.board[x][y] == 'X') or (Gm.user_board.board[x][y] == '-'):
                continue
            else:
                break


        return [x, y]

class User (Player):
    @staticmethod
    def name():
        return 'Игрок'
    def ask(self):
        while True:
            try:
                shooting_crd = int(input('Введите точку, в которую будем стрелять, например, 11:'))
            except ValueError:
                print('Вы ввели что-то не то! Попробуйте еще раз')
                continue

            if shooting_crd not in [11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26, 31, 32, 33, 34, 35, 36, 41, 42, 43, 44, 45, 46, 51, 52, 53, 54, 55, 56, 61, 62, 63, 64, 65, 66]:
                print('Введите координату доски, которая есть на игровом поле!')
                continue

            crd = [int(i) for i in str(shooting_crd)]
            if (self.opp_board.board[crd[0]][crd[1]] == 'X') or (self.opp_board.board[crd[0]][crd[1]] == '-'):
                print('Это поле уже обстреляно! Выберите другое.')
                continue
            else:
                break

        return crd

class Game:
    def __init__(self, user, user_board, ai_player, ai_board):
        self.user = user
        self.dot1 = user_board
        self.dot2 = ai_board
        self.user_board = user.my_board
        self.ai_player = ai_player
        self.ai_board = ai_player.my_board


    def loop(self): #вызываем метод mode и проверяем, сколько кораблей ок
        return


    def gameplay(self):
        ships_list = [3, 2, 2, 1, 1, 1, 1]
        ships_status = {3: [3], 2: [2, 2], 1: [1, 1, 1, 1]}
        player_board = Board(self.user_board, ships_list, self.user, ships_status)
        ai_board = Board(self.ai_board, ships_list, self.ai_player, ships_status)
        while True:
            print('Моя доска')
            print(str(self.user_board))
            print('Военная доска')
            print(str(player_board.player.opp_board))
            a = player_board.shot()
            player_opp_lifes = player_board.win_check()
            if player_opp_lifes == 0:
                print(f'Победил {player_board.player.name()}')
                break
            else:
                print(f'{player_board.player.name()} должен совершить еще {player_opp_lifes} попаданий')
            if a:
                continue
            b = True
            while b:
                b = ai_board.shot()
                ai_opp_lifes = ai_board.win_check()
                if ai_opp_lifes == 0:
                    print(f'Победил {ai_board.player.name()}')
                    break
                else:
                    print(f'{ai_board.player.name()} должен совершить еще {ai_opp_lifes} попаданий')

    def start(self):
        print('Тут должны быть правила игры и приветственное слово')
        self.user_board = Dot()
        print(str(self.user_board))
        ship_rules = ['3', '2', '2', '1', '1', '1', '1']
        ships_list = []
        ships_status = []
        user_board = Board(user_dot, ships_list, user, ships_status)
        for ship_len in ship_rules[:3]:
             while True:
                ship_property = user_board.add_ship(ship_len)
                ship = Ship(*ship_property)
                info = ship.add_to_board()
                coord = [int(i) for i in str(info[0])]
                if ship_len == '3':
                    try:
                        if info[1] and self.user_board.board[coord[0]][coord[1]] == '0' and self.user_board.board[coord[0]][coord[1]+1] == '0' and self.user_board.board[coord[0]][coord[1]+2] == '0':
                            self.user_board.board[coord[0]][coord[1]] = '■'
                            self.user_board.board[coord[0]][coord[1]+1] = '■'
                            self.user_board.board[coord[0]][coord[1]+2] = '■'
                            try:
                                if self.user_board.board[coord[0]+1][coord[1]] == '0':
                                    self.user_board.board[coord[0]+1][coord[1]] = 'O'
                            except IndexError:
                                pass
                            try:
                                if self.user_board.board[coord[0]-1][coord[1]] == '0':
                                    self.user_board.board[coord[0]-1][coord[1]] = 'O'
                            except IndexError:
                                pass
                            try:
                                if self.user_board.board[coord[0]][coord[1]-1] == '0':
                                    self.user_board.board[coord[0]][coord[1]-1] = 'O'
                            except IndexError:
                                pass
                            try:
                                if self.user_board.board[coord[0]+1][coord[1]+1] == '0':
                                    self.user_board.board[coord[0]+1][coord[1]+1] = 'O'
                            except IndexError:
                                pass
                            try:
                                if self.user_board.board[coord[0]-1][coord[1]+1] == '0':
                                    self.user_board.board[coord[0]-1][coord[1]+1] = 'O'
                            except IndexError:
                                pass
                            try:
                                if self.user_board.board[coord[0]+1][coord[1]+2] == '0':
                                    self.user_board.board[coord[0]+1][coord[1]+2] = 'O'
                            except IndexError:
                                pass
                            try:
                                if self.user_board.board[coord[0]-1][coord[1]+2] == '0':
                                    self.user_board.board[coord[0]-1][coord[1]+2] = 'O'
                            except IndexError:
                                pass
                            try:
                                if self.user_board.board[coord[0]][coord[1]+3] == '0':
                                    self.user_board.board[coord[0]][coord[1]+3] = 'O'
                            except IndexError:
                                pass
                            print(str(self.user_board))
                            break
                        elif info[1] is False and self.user_board.board[coord[0]][coord[1]] == '0' and self.user_board.board[coord[0]+1][coord[1]] == '0' and self.user_board.board[coord[0]+2][coord[1]+2] == '0':
                            self.user_board.board[coord[0]][coord[1]] = '■'
                            self.user_board.board[coord[0]+1][coord[1]] = '■'
                            self.user_board.board[coord[0]+2][coord[1]] = '■'
                            try:
                                if self.user_board.board[coord[0]][coord[1]+1] == '0':
                                   self.user_board.board[coord[0]][coord[1]+1] = 'O'
                            except IndexError:
                                pass
                            try:
                                if self.user_board.board[coord[0]][coord[1]-1] == '0':
                                    self.user_board.board[coord[0]][coord[1]-1] = 'O'
                            except IndexError:
                                pass
                            try:
                                if self.user_board.board[coord[0]-1][coord[1]] == '0':
                                    self.user_board.board[coord[0]-1][coord[1]] = 'O'
                            except IndexError:
                                pass
                            try:
                                if self.user_board.board[coord[0]+1][coord[1]+1] == '0':
                                    self.user_board.board[coord[0]+1][coord[1]+1] = 'O'
                            except IndexError:
                                pass
                            try:
                                if self.user_board.board[coord[0]+1][coord[1]-1] == '0':
                                    self.user_board.board[coord[0]+1][coord[1]-1] = 'O'
                            except IndexError:
                                pass
                            try:
                                if self.user_board.board[coord[0]+2][coord[1]+1] == '0':
                                    self.user_board.board[coord[0]+2][coord[1]+1] = 'O'
                            except IndexError:
                                pass
                            try:
                                if self.user_board.board[coord[0]-2][coord[1]+1] == '0':
                                    self.user_board.board[coord[0]-2][coord[1]+1] = 'O'
                            except IndexError:
                                pass
                            try:
                                if self.user_board.board[coord[0]+3][coord[1]] == '0':
                                    self.user_board.board[coord[0]+3][coord[1]] = 'O'
                            except IndexError:
                                pass
                            print(str(self.user_board))
                            break
                        else:
                            print('Не получилось разместить корабль, попробуйте еще раз')
                    except IndexError:
                        print('Не получилось разместить корабль, попробуйте еще раз')
                        continue
                elif ship_len == '2':
                    try:
                        if info[1] and self.user_board.board[coord[0]][coord[1]] == '0' and self.user_board.board[coord[0]][coord[1]+1] == '0':
                            self.user_board.board[coord[0]][coord[1]] = '■'
                            self.user_board.board[coord[0]][coord[1]+1] = '■'
                            try:
                                if self.user_board.board[coord[0]+1][coord[1]] == '0':
                                    self.user_board.board[coord[0]+1][coord[1]] = 'O'
                            except IndexError:
                                pass
                            try:
                                if self.user_board.board[coord[0]-1][coord[1]] == '0':
                                    self.user_board.board[coord[0]-1][coord[1]] = 'O'
                            except IndexError:
                                pass
                            try:
                                if self.user_board.board[coord[0]][coord[1]-1] == '0':
                                    self.user_board.board[coord[0]][coord[1]-1] = 'O'
                            except IndexError:
                                pass
                            try:
                                if self.user_board.board[coord[0]+1][coord[1]+1] == '0':
                                    self.user_board.board[coord[0]+1][coord[1]+1] = 'O'
                            except IndexError:
                                pass
                                if self.user_board.board[coord[0]-1][coord[1]+1] == '0':
                                    self.user_board.board[coord[0]-1][coord[1]+1] = 'O'
                            try:
                                if self.user_board.board[coord[0]][coord[1]+2] == '0':
                                    self.user_board.board[coord[0]][coord[1]+2] = 'O'
                            except IndexError:
                                pass
                            print(str(self.user_board))
                            break
                        elif info[1] is False and self.user_board.board[coord[0]][coord[1]] == '0' and self.user_board.board[coord[0]+1][coord[1]] == '0':
                            self.user_board.board[coord[0]][coord[1]] = '■'
                            self.user_board.board[coord[0]+1][coord[1]] = '■'
                            try:
                                if self.user_board.board[coord[0]][coord[1]+1] == '0':
                                    self.user_board.board[coord[0]][coord[1]+1] = 'O'
                            except IndexError:
                                pass
                            try:
                                if self.user_board.board[coord[0]][coord[1]-1] == '0':
                                    self.user_board.board[coord[0]][coord[1]-1] = 'O'
                            except IndexError:
                                pass
                            try:
                                if self.user_board.board[coord[0]-1][coord[1]] == '0':
                                    self.user_board.board[coord[0]-1][coord[1]] = 'O'
                            except IndexError:
                                pass
                            try:
                                if self.user_board.board[coord[0]+1][coord[1]+1] == '0':
                                    self.user_board.board[coord[0]+1][coord[1]+1] = 'O'
                            except IndexError:
                                pass
                            try:
                                if self.user_board.board[coord[0]+1][coord[1]-1] == '0':
                                    self.user_board.board[coord[0]+1][coord[1]-1] = 'O'
                            except IndexError:
                                pass
                            try:
                                if self.user_board.board[coord[0]+2][coord[1]] == '0':
                                    self.user_board.board[coord[0]+2][coord[1]] = 'O'
                            except IndexError:
                                pass
                            print(str(self.user_board))
                            break
                        else:
                            print('Не получилось разместить корабль, попробуйте еще раз')
                    except IndexError:
                        print('Не получилось разместить корабль, попробуйте еще раз')
                        continue
                else:
                    break


        check = 0
        while check != 4:
            while True:
                try:
                    coord = int(input('Введите точку, где будет расположен нос корабля, например, 11:'))
                except ValueError:
                    print('Вы ввели что-то не то! Попробуйте еще раз')
                    continue
                if coord not in [11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26, 31, 32, 33, 34, 35, 36, 41, 42, 43, 44, 45, 46, 51, 52, 53, 54, 55, 56, 61, 62, 63, 64, 65, 66]:
                    print('Введите координату доски, которая есть на игровом поле!')
                    continue
                coord = [int(i) for i in str(coord)]
                if self.user_board.board[coord[0]][coord[1]] == '0':
                    self.user_board.board[coord[0]][coord[1]] = '■'
                    check += 1
                    try:
                        if self.user_board.board[coord[0]+1][coord[1]] == '0':
                            self.user_board.board[coord[0]+1][coord[1]] = 'O'
                    except IndexError:
                        pass
                    try:
                        if self.user_board.board[coord[0]-1][coord[1]] == '0':
                            self.user_board.board[coord[0]-1][coord[1]] = 'O'
                    except IndexError:
                        pass
                    try:
                        if self.user_board.board[coord[0]][coord[1]+1] == '0':
                            self.user_board.board[coord[0]][coord[1]+1] = 'O'
                    except IndexError:
                        pass
                    try:
                        if self.user_board.board[coord[0]][coord[1]-1] == '0':
                            self.user_board.board[coord[0]][coord[1]-1] = 'O'
                    except IndexError:
                        pass
                    print(str(self.user_board))
                    break
                else:
                    print('Клетка уже занята, выберите другую')
                    continue

        print('Расстановка кораблей завершена, приготовьтесь к бою')
        self.gameplay()


ai_dot = Dot()
opp_board_for_user = Dot()
opp_board_for_ai = Dot()
user_dot = Dot()
user = User(user_dot, opp_board_for_user, ai_dot)
ai = AI(ai_dot, opp_board_for_ai, user_dot)


def place_ships(dot, ship_rules=[3,2,2,1,1,1,1]):
    board = dot.board
    for ship in ship_rules:
        valid_placement = False
        while not valid_placement:
            orientation = random.choice(['horizontal', 'vertical'])
            if orientation == 'horizontal':
                x = random.randint(1, 7 - ship)
                y = random.randint(1, 6)
            elif orientation == 'vertical':
                x = random.randint(1, 6)
                y = random.randint(1, 7 - ship)
            valid_placement = check_placement(board, x, y, ship, orientation)
        place_ship(board, x, y, ship, orientation)

def check_placement(board, x, y, ship, orientation):
    for i in range(ship):
        try:
            if orientation == 'horizontal':
                if board[y][x+i] != '0' or board[y+1][x+i] != '0' or board[y-1][x+i] != '0':
                    return False
            elif orientation == 'vertical':
                if board[y+i][x] != '0' or board[y+i][x+1] != '0' or board[y+i][x-1] != '0':
                    return False
        except IndexError:
            pass
    return True

def place_ship(board, x, y, ship, orientation):
    for i in range(ship):
        try:
            if orientation == 'horizontal':
                board[y][x+i] = '■'
                board[y-1][x+i] = 'O'
                board[y+1][x+i] = 'O'
            elif orientation == 'vertical':
                board[y+i][x] = '■'
                board[y+i][x-1] = 'O'
                board[y+i][x+1] = 'O'
        except IndexError:
            pass
    try:
        if orientation == 'horizontal':
            if x - 1 >= 1:
                board[y][x-1] = 'O'
            if x + ship <= 6:
                board[y][x+ship] = 'O'
        elif orientation == 'vertical':
            if y - 1 >= 1:
                board[y-1][x] = 'O'
            if y + ship <= 6:
                board[y+ship][x] = 'O'
    except IndexError:
        pass


place_ships(ai_dot)
Gm = Game(user, user_dot, ai, ai_dot)
Gm.start()
