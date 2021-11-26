import random

numberList = [111, 222, 333, 444, 555]
print(random.choices(numberList, weights=(10, 10, 10, 10, 60), k=5 ))


katigories = [sword, potion, ring]
sword_items = ["woodensword", "lightsabre"]

def item_type_decider():
    item_type = random.choices(katigories, weights=(40, 20, 40), k=2 ))
    return item_type


new_item_kategory = item_type_decider()

if 




