'''
Вариант Б.  Вариант предметной области - 10
Задание 1
- «Компьютер» и «Браузер» связаны соотношением один-ко-многим. 
Выведите список всех связанных Браузеров и Компьютеров, 
отсортированный по Компьютерам, сортировка по Браузерам произвольная.

Задание 2
- «Компьютер» и «Браузер» связаны соотношением один-ко-многим. Выведите 
список Браузеров с количеством Компьютеров которые используют 
этот браузер, отсортированный по количеству Браузеров.

Задание 3
- «Компьютер» и «Браузер» связаны соотношением многие-ко-многим. 
Выведите список всех Компьютеров, диагональ которых равна 14, 
и названия Браузеров, которые на них стоят.

'''
from operator import itemgetter
class Comp:                         #класс Компьютеров
    def __init__(self, id, name, diagonal, browser_id):
        self.id = id
        self.name = name
        self.diagonal = diagonal
        self.browser_id = browser_id

class Browser:                      #класс Браузеров
    def __init__(self, id, name):
        self.id = id
        self.name = name

class CompBrowser:                          #класс для реализации многие ко многим
    def __init__(self, comp_id, browser_id):
        self.comp_id = comp_id
        self.browser_id = browser_id


Comps = [                               #список Компьютеров
    Comp(1, 'Acer', 15.6, 4),               
    Comp(2, 'Asus', 17, 2),                 
    Comp(3, 'Honor', 14, 3),                
    Comp(4, 'Microsoft surface', 15.6, 4),  
    Comp(5, 'Lenovo', 14, 1),               
    Comp(6, 'Macbook', 13.6, 3),            
    Comp(7, 'MSI', 14, 3),                  
]



Browsers = [                               #список Браузеров
    Browser(1, 'Tor'),              
    Browser(2, 'Firefox'),          
    Browser(3, 'Google Chrome'),    
    Browser(4, 'Microsoft Edge'),   
]

CompBrowsers = [
    CompBrowser(1, 4),
    CompBrowser(2, 2),
    CompBrowser(3, 3),
    CompBrowser(4, 4),
    CompBrowser(5, 1),
    CompBrowser(6, 3),
    CompBrowser(7, 3),
    CompBrowser(5, 2)
]

def main():

     # Соединение данных один-ко-многим
    one_to_many = [(c.name, c.diagonal, b.name)
        for b in Browsers
        for c in Comps
        if c.browser_id == b.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(b.name, compbrowser.browser_id, compbrowser.comp_id)
    for b in Browsers
    for compbrowser in CompBrowsers
    if b.id == compbrowser.browser_id]

    many_to_many = [(c.name, c.diagonal, browser_name)
    for browser_name, browser_id, comp_id in many_to_many_temp 
    for c in Comps if c.id == comp_id]

    print('Задание Б1')             #выполнение 1ой задачи
    res_b1 = sorted(one_to_many, key = itemgetter(0))
    print(res_b1)

    print('\nЗадание Б2')             #выполнение 2ой задачи
    a = list(set([i.name for i in Browsers]))
    res_b2 = sorted([(i, len([j for j in many_to_many_temp if i == j[0]])) for i in a], key = itemgetter(1)) 
    print(res_b2)

    print('\nЗадание Б3')             #выполнение 3ой задачи
    b = [j for j in many_to_many if j[1] == 14]
    res_b3 = {j[2]: [i[0] for i in b if i[2] == j[2]] for j in b}
    print(res_b3)


if __name__ == '__main__':
    main()










'''
for c in Comps:
        if c.diagonal == 14:
            #print(c.name)
            c_browsers = list(filter(lambda i: i[0]==c.diagonal, many_to_many))
            c_browsers_diagonals = [x for x,_,_ in c_browsers]
            res_b3[c.diagonal] = c_browsers_diagonals



'''