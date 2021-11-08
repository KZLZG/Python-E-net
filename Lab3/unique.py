from gen_random import gen_random

# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):

        ''' Нужно реализовать конструктор
В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
Например: ignore_case = True, Aбв и АБВ - разные строки
          ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
        По-умолчанию ignore_case = False'''


        self.items = iter(items)

        self.seen = set()

        self.ignore_case = kwargs.get('ignore_case')



    def __iter__(self):

        return self





    def __next__(self):

        if self.ignore_case != True:

            while True:

                next_item = next(self.items)

                if (next_item.lower() not in self.seen) and (next_item not in self.seen):

                    self.seen.add(next_item)

                    return next_item

        else:

            while True:

                next_item = next(self.items)

                if next_item not in self.seen:

                    self.seen.add(next_item)

                    return next_item





'''

alph = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']

print('False')

for item in Unique(alph, ignore_case=False):

    print(item)



print('True')

for item in Unique(alph, ignore_case=True):

    print(item)
'''
