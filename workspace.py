# MTG life counter CLI application
# This will be my first project that I will code from scratch using concepts I'm learning on Boot.dev
# This is a work in progress so take my commits as steps towards the final completion of this idea

# def player_one():


# def player_two():


# def main():
#     print("-----------------")
#     print(f"Player One life total: {life_total}")
#     print(f"Player Two life total: {life_total}")

def player(life_total, damage, healing):
    life_total += healing
    life_total -= damage
    remaining_life = life_total
    return remaining_life

# print(player(20, 6, 0))
    
    