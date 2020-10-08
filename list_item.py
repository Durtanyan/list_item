# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 20:30:53 2020

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

#Парсим строку в лист листов через .split().
# Сначала по переносу строки ('\n'), затем по (';') 
#используем ListComprehension
list_string = [string.split(';') for string in [string for string in log.split('\n')]]

#Используя DictComprehension парсим 
#ListComprehension в словарь		
dict_item_and_itemcost= {string[2].split(':')[1] : string[3].split(':')[1] \
                        for string in list_string if int(string[3].split(':')[1]) < 13000}

#Используя ListComprehension распарсиваем словарь, 
#полученный с помощью DictComprehension по ключам,
# полученный список выводим на печать
list_item = [key for key in dict_item_and_itemcost.keys()]

print('____________________________________')
print('| Список наименований товаров,     |\n| у которых item_cost меньше 13000.|')
print('____________________________________')

for i in list_item:
    print(f'| {i:32} |')
print('|__________________________________|')

