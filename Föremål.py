def item_type_decider():
    type = rand.randint(1, 100)
    if type == (1, 40):
        type_of_item = "sword"
    elif type == (41, 60):
        type_of_item = "ring"
    elif type == (61, 100):
        type_of_item = "potion"

def item_type_sword():
    rarity = rand.randint(1, 100)
    if rarity == (1, 50):
        return(wooden_sword)
    if rarity == (51, 100):
        return(laser_saber)


print("Öppnar chista")