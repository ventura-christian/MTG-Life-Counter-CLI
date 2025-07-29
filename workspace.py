# MTG LIFE COUNTER CLI APPLICATION
# This will be my first project that I will code from scratch using concepts I'm learning on Boot.dev
# This is a work in progress so take my commits as steps towards the final completion of this idea

# What do I want to achieve?
# 1: I want to define the number of players
# 2: I want to create life totals for the designated amount of players
# 3: I want to print the players and their associated life totals
# 4: I want to assign damage or healing to any of the players then return the current life totals after interaction
# 5: I want to store the current state of the life totals for the respective players and update the life totals after each interaction
# 6: I want to print a clean statement that displays all of the players names and current life totals after each interaction and will prompt for more interactions 

# Current attempt to create a player and the code to handle the interaction math
def player(life_total, damage, healing):
    life_total += healing
    life_total -= damage
    remaining_life = life_total
    return remaining_life

print(player(20, 0, 10))
    
    