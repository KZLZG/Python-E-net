import pytest
from RK1 import *



def test_answer1():
    one_to_many = [(c.name, c.diagonal, b.name)
        for b in Browsers
        for c in Comps
        if c.browser_id == b.id]
    assert res_b1(one_to_many) == [('Acer', 15.6, 'Microsoft Edge'), ('Asus', 17, 'Firefox'), 
                                    ('Honor', 14, 'Google Chrome'), 
                                    ('Lenovo', 14, 'Tor'), ('MSI', 14, 'Google Chrome'), 
                                    ('Macbook', 13.6, 'Google Chrome'), 
                                    ('Microsoft surface', 15.6, 'Microsoft Edge')]

def test_answer2():
    many_to_many_temp = [(b.name, compbrowser.browser_id, compbrowser.comp_id)
        for b in Browsers
        for compbrowser in CompBrowsers
        if b.id == compbrowser.browser_id]
    assert res_b2(many_to_many_temp) == [('Tor', 1), ('Firefox', 2), 
                                        ('Microsoft Edge', 2), ('Google Chrome', 3)]

def test_answer3():
    many_to_many_temp = [(b.name, compbrowser.browser_id, compbrowser.comp_id)
        for b in Browsers
        for compbrowser in CompBrowsers
        if b.id == compbrowser.browser_id]
    many_to_many = [(c.name, c.diagonal, browser_name)
        for browser_name, browser_id, comp_id in many_to_many_temp 
        for c in Comps if c.id == comp_id]
    assert res_b3(many_to_many) == {'Tor': ['Lenovo'], 'Firefox': ['Lenovo'],
                                     'Google Chrome': ['Honor', 'MSI']}

if __name__ == '__main__':
    pytest.main()



