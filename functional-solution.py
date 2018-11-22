#!/usr/bin/env python3

import json


def sort(list1, key):
    list2 = list1[:]
    list2.sort(key=key)
    return list2


with open('beer_list.json') as file:
    beer_list = json.load(file)

sorted_beer_list = sort(beer_list, lambda elem: elem['Tx_Alcool'] if elem['Tx_Alcool'] else -1)

for beer in sorted_beer_list:
    print(beer['Nom'], beer['Tx_Alcool'])
