import json

import sys

# Сделаем другие необходимые импорты

import cm_timer

import field

from gen_random import gen_random

from print_result import print_result

#from sort import result

from unique import Unique

#import pathlib

import os




path = os.path.abspath('data_light.json')

# Необходимо в переменную path сохранить путь к файлу, который был 

# передан при запуске сценария



with open(path) as f:

    data = json.load(f, encoding='utf-8')



# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`

# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку

# В реализации функции f4 может быть до 3 строк

'''Функция f1 должна вывести отсортированный список профессий без повторений 

(строки в разном регистре считать равными). Сортировка должна игнорировать 

регистр. Используйте наработки из предыдущих задач.

'''



@print_result

def f1(arg):

    res =[]

    test_field = field.field(arg, "job-name")

    while True:

        try:

            res.append(next(test_field))

        except StopIteration:

            break

    

    return list(Unique(sorted(res)))





@print_result

def f2(arg):

    return list(filter(lambda x: 'программист' in x, arg))

  





@print_result

def f3(arg):

    return list(map(lambda x: x + ' с опытом Python', arg))







@print_result

def f4(arg):

    sum = []

    for i in gen_random(len(arg), 100000, 200000):

        sum.append(i)

    return list(zip(arg, sum))





if __name__ == '__main__':

    with cm_timer.cm_timer_1():

        f4(f3(f2(f1(data))))

