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


def res_b1(inp):
    a = sorted(inp, key = itemgetter(0))
    return a

def res_b2(many_to_many_temp):
    a = list(set([i.name for i in Browsers]))
    return sorted([(i, len([j for j in many_to_many_temp if i == j[0]])) for i in a], key = itemgetter(1)) 

def res_b3(many_to_many):
    b = [j for j in many_to_many if j[1] == 14]
    return {j[2]: [i[0] for i in b if i[2] == j[2]] for j in b}



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


    print('Задание Б1')
    result1 =  res_b1(one_to_many)            #выполнение 1ой задачи    
    print(result1)
    
    print('\nЗадание Б2')             #выполнение 2ой задачи
    print(res_b2(many_to_many_temp))

    print('\nЗадание Б3')             #выполнение 3ой задачи
    print(res_b3(many_to_many))

if __name__ == '__main__':
    main()






 #res_b1 = sorted(one_to_many, key = itemgetter(0))
''' a = list(set([i.name for i in Browsers]))
    res_b2 = sorted([(i, len([j for j in many_to_many_temp if i == j[0]])) for i in a], key = itemgetter(1)) 
    print(res_b2) '''

''' b = [j for j in many_to_many if j[1] == 14]
    res_b3 = {j[2]: [i[0] for i in b if i[2] == j[2]] for j in b}
    print(res_b3)'''