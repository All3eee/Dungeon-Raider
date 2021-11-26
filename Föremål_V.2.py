import random
from types import new_class


katigories = ['sword', 'potion', 'ring']
sword_items = ["woodensword", "lightsaber"]

def item_type_decider():
    item_type = random.choices(katigories, weights=(40, 20, 40), k=1 )
    return item_type

def item_kategory_sword():
    item_sword = random.choices(sword_items, weights=(50, 50), k=1)
    return item_sword


new_item_kategory = item_type_decider()
new_sword_item = item_kategory_sword()
h = new_sword_item.pop(0)
print(h)

swords = {
    "woodensword": 2,
    "lightsaber": 1000,
}

s = 0
s += swords[h]
print(s)
