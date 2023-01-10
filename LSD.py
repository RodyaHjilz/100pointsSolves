import re
from random import choice, randint


class CorrectNumbers:
    # Базовый оператор инициализации класса
    def __init__(self, n):
        self.n = n
        # В этом списке будут валидные номера
        self.list_of_numbers = [self.generating_numbers() for _ in range(self.n)]

    # Сортировка по ЛСД
    def sorting_numbers(self, number):
        pass

    def generating_numbers(self):
        letters = 'АВЕКМНОРСТУХ'
        result = ''
        nums = [str(i).zfill(2) for i in range(300)]
        for i in range(1, 10):
            if i == 1 or 4 < i < 7:
                result += choice(letters)
            elif 1 < i < 5:
                result += str(randint(1, 9))
        result += choice(nums)
        return result

    def get_numbers(self):
        return '\n'.join(self.list_of_numbers)


# Создали 1000 валидных номеров и после некоторых преобразований вернули валидный список из N Номеров
N = int(input())
example = CorrectNumbers(N)
print(example.get_numbers())
