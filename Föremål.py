from random import randint

class Item():
    
    def __init__(self):
        self.item_type = self.item_type_decider(randint(1, 100))
        self.item_type_dict = {"sword": "self.item_type_sword(randint(1, 100))",
        "potion": "2",
        "ring": "2"
        }
        self.item = eval(self.item_type_dict[self.item_type])
        self.item_strengh = {"lightsaber": 10}

    def item_type_decider(self, new_type_of_item):
        if new_type_of_item in list(range(1, 40)):
            return "sword"
        elif new_type_of_item in list(range(41, 60)):
            return "ring"
        elif new_type_of_item in list(range(61, 100)):  
            return "potion"

    def item_type_sword(self, new_item_type):
        if new_item_type in list(range(1, 50)):
            return "wooden_sword"
            
        elif new_item_type in list(range(51, 100)):
            return "lightsaber"


h = 1

if h == 1:
    new_item = Item()
    print(new_item.item)


'''
Göra dictionary och sedan keys
'''