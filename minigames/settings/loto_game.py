import random


# создание класса мешка с боченками
class BarrelBag():

    def __init__(self):
        self.barrel_list = []
        self.barrel_pop = []
        self.barrel_other = 111

    """Создание мешка с бочонками"""

    def create_barrel(self):
        for i in range(1, 100):
            self.barrel_list.append(i)

        """Метод возвращает рандомно выбранный боченок
        это под вопросом?"""

    def get_barrel(self):
        barrel = random.choice(self.barrel_list)
        index_barrel = self.barrel_list.index(barrel)
        if len(self.barrel_pop) == 5:
            self.barrel_other = self.barrel_pop[0]
            self.barrel_pop.remove(self.barrel_pop[0])

        self.barrel_pop.append(self.barrel_list.pop(index_barrel))

    """Метод удаляет бочонок из мешка"""

    def del_barrel(self, barrel):
        self.barrel_list.remove(barrel)


# создание класса билета
class Ticket():

    def __init__(self):
        # Сдесь хранятся все взятые билеты игроком
        self.ticket_list = []

    """Исправить ошибку в логике выдает одинаковые значения
    проработать инструкцию if
    вывод метода
    |0|0|46|0|5|2|0|1|0|
    |0|58|0|83|0|45|0|69|0|
    |0|0|9|0|10|0|14|0|78|"""

    def create_ticket(self):
        ticket = []

        for x in range(3):
            line_ticket = [0 for i in range(9)]
            while line_ticket.count(0) != 4:
                choice_number = random.choice(range(1, 100))
                choice_index = random.choice(range(0, 8))
                if not ticket.count(choice_number):
                    line_ticket[choice_index] = choice_number
            ticket.append(line_ticket)

        self.ticket_list.append(ticket)
        return ticket

    """Изменить билет: В параметры модуля поступают значения
    билета и номер боченка, и возвращает изменненый билет вида
    переменные a,b временно для PEP-8
    |--|--|46|--|-5|XX|--|-1|--|
    |--|58|--|83|--|45|--|69|--|
    |--|--|-9|--|10|--|14|--|78|"""

    def cross_it_uot(self, ticket, number):

        if len(self.ticket_list) >= 1:
            tickets = self.ticket_list[ticket]
            for i in tickets:
                if number in i:
                    a, b = tickets.index(i), i.index(number)
                    self.ticket_list[ticket][a][b] = 0

    """Метод принимает на вход число проверяет есть ли оно в билете
    если ДА вычеркивает, так же проверяет остались ли еще числа не равные
    0 в билете
    переменные a,b временно для PEP-8"""

    def check_ticket(self, check_num=None):

        if check_num:
            if len(self.ticket_list) >= 1:
                for i in self.ticket_list:
                    for j in i:
                        if check_num in j:
                            a, b = self.ticket_list.index(i), i.index(j)
                            self.ticket_list[a][b][j.index(check_num)] = 111

    """Удалить билет"""

    def delete_ticket(self):
        pass


# Класс игрока
class Player():

    """Создать игрока"""
    def create_player(self):
        pass

    """Ход игрока"""
    def move_player(self):
        pass


class Game():

    def __init__(self):
        pass


if __name__ == '__main__':
    pass
