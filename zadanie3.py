class Tomato:
    states = {1: 'Зелено-зрелые томаты', 2: 'Бланжевые томаты', 3: 'Полностью спелые томаты'}

    def __init__(self, index):
        self._index = index
        self._state = 1

    def grow(self):
        if self._state < 3:
            self._state += 1
            print('Стадия созревания:', Tomato.states[self._state])

    def is_ripe(self):
        if self._state == 3:
            return True
        else:
            return False


class TomatoBush:
    def __init__(self, number_tomato):
        self.tomatoes = [Tomato(i) for i in range(number_tomato)]

    def grow_all(self):
        for tomat in self.tomatoes:
            tomat.grow()

    def all_are_ripe(self):
        a = 0
        for tomat in self.tomatoes:
            if tomat.is_ripe():
                pass
            else:
                a += 1
        if a > 0:
            return False
        else:
            return True


    def give_away_all(self):
        self.tomatoes = []

class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant


    def work(self):
        self._plant.grow_all()


    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Помидоры собраны.')
        else:
            print('Помидоры ещё не созрели.')

    @staticmethod
    def knowledge_base():
        print('Садовник Иванов Иван Иванович')



Gardener.knowledge_base()
tomato_farm = TomatoBush(2)
Farmer = Gardener('Иванов Иван Иванович', tomato_farm)
Farmer.work()
Farmer.harvest()
Farmer.work()
Farmer.harvest()