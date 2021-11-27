import random


katigories = ['sword', 'potion', 'ring']
sword_items = ["woodensword", "lightsaber"]
ring_items = ['force ring', 'ring of fire']

def item_type_decider():
    item_type = random.choices(katigories, weights=(40, 20, 40), k=1 )
    return item_type

def item_kategory_sword():
    item_sword = random.choices(sword_items, weights=(50, 50), k=1)
    return item_sword

def item_kategory_ring():
    item_ring = random.choices(ring_items, weights=(10, 50, 40), k=1)
    return item_ring


new_item_kategory = item_type_decider()
new_sword_item = item_kategory_sword()
h = new_sword_item.pop(0)
print(h)

vi()

'''
s = 0
s += swords[h]
print(s)
'''