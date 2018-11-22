#!/usr/bin/env python3

import json

with open('beer_list.json') as file:
    beer_list = json.load(file)

beer_list.sort(key=lambda elem: elem['Tx_Alcool'] if elem['Tx_Alcool'] else -1)

# for i in range(len(beer_list)):
#     min = beer_list[i]["Tx_Alcool"]
#     index = i
#     for j in range(i+1, len(beer_list)):
#         if beer_list[j]["Tx_Alcool"] is None:
#             beer_list[j]["Tx_Alcool"] = -1
#         if min > beer_list[j]["Tx_Alcool"]:
#             min = beer_list[j]["Tx_Alcool"]
#             index = j
#     beer_list[i], beer_list[index] = beer_list[index], beer_list[i]

for beer in beer_list:
    print(beer['Nom'], beer['Tx_Alcool'])
