# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 15:37:14 2020

@author: lukin
"""
"""
Задача: вывести список наименований товаров, у которых item_cost меньше 13000
"""

log = """name:Иван;gender:m;item:Часы;item_cost:9800
name:Иван;gender:m;item:Фитнес-браслет;item_cost:12300
name:Иван;gender:m;item:Кофемашина;item_cost:23500
name:Петр;gender:m;item:Часы;item_cost:9800
name:Петр;gender:m;item:Фитнес-браслет;item_cost:12300
name:Петр;gender:m;item:Айфон;item_cost:77900
name:Петр;gender:m;item:Чехол для телефона;item_cost:350
name:Петр;gender:m;item:Кофемашина;item_cost:23500
name:Дарья;gender:m;item:Айфон;item_cost:77900
name:Марья;gender:m;item:Кофемашина;item_cost:23500
name:Юлия;gender:m;item:Фитнес-браслет;item_cost:12300"""

elements = log.split('\n')
dict_item_cost = dict()
set_dict = set()
for element in elements:
    i = element.split(';')
    for j in range(len(i)):
        dict_item_cost[i[j].split(':')[0]] = i[j].split(':')[1]
    if int(dict_item_cost['item_cost']) < 13000:
        set_dict.add(dict_item_cost['item'])
print('Список товаров цена которых меньше 13000:')
for i in set_dict:
    print(i)

    