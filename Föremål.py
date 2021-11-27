import random

class Item():

    def __init__(self, kategories, sword_items, ring_items, potion_items) :
        self.kategories = kategories
        self.sword_items = sword_items
        self.ring_items = ring_items
        self.potion_items = potion_items

    def item_type_decider(self):
        item_type = random.choices(self.kategories, weights=(40, 20, 40), k=1 )
        return item_type

    def item_kategory_sword(self):
        item_sword = random.choices(self.sword_items, weights=(50, 50), k=1)
        return item_sword

    def item_kategory_ring(self):
        item_ring = random.choices(self.ring_items, weights=(10, 50, 40), k=1)
        return item_ring
    
    def item_kategory_potion(self):
        item_potion = random.choices(self.potion_items, weights=(50, 50), k=1)


list_kategories = ['Sword', 'Potion', 'Ring']  
list_swords = ["Woodensword", "Lightsaber"]
list_rings =  ['Force ring', 'Ring of fire']
list_potion = ['Health potion', 'Strenght potion']

Player1 = Item(list_kategories, list_swords, list_rings, list_potion)

def open_chest():   
    new_item_kategory = Player1.item_type_decider()
    
    if new_item_kategory == 'sword':
        new_sword_item = Player1.item_kategory_sword()
        h = new_sword_item.pop(0)
        print(h)

    elif new_item_kategory == 'ring':
        new_ring_item = Player1.item_kategory_ring()
        print(new_ring_item.pop())

    elif new_item_kategory == 'potion':
        new_potion_item = Player1.item_kategory_potion()
        print(new_potion_item.pop(0))

while True:
    open_chest()

'''
swords = {
    "woodensword": 2,
    "lightsaber": 1000,
}

s = 0
s += swords[h]
print(s)
'''