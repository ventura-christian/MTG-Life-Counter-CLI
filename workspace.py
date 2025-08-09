print("========================")
print("Welcome to AetherPulse\nThe simple to use Magic the Gathering life tracker")
print("========================")
player_one = input("Please enter your name: ")
player_name = player_one.capitalize()
starting_life_total = int(input("Please enter your current life total: "))

print("========================")
print(f"Match started\n{player_name} begins the game with {starting_life_total} life.")

def player_options():
    options = int(input("Please make a selection:\n1 Gain Life\n2 Lose Life\n3 Exit program\nSelection: "))
    while options != 3:
        if options == 1:
            gained_life = input("How much life is gained? ")
            calcultion = starting_life_total + int(gained_life)
            current_life_total = calcultion
            print(f"{player_name} now has {current_life_total} life.") 
            return player_options()
        # THIS IS WHERE I LEFT OFF!!
        # Continue figuring out how to store the new, updated life totals after each change occurs
        elif options == 2:
            life_lost = input("How much life is lost? ")
            current_life_total = starting_life_total - int(life_lost)
            print(f"{player_name} now has {current_life_total} life.")
            return player_options()

    return "Thank you for using AetherPulse!"

print(player_options())
            
    
    

    
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
    
        
# def player_status:
# I need this to accept inputs for taking damage and gaining health. 
# I need to assign this to each player individually and allow for each player to be affected without changing the other players life totals or status changes

# def player:
# I need this to be assigned to each individual player and allow for the player's name
# I want this to be able to assign a title to each player individually, EX: "player 1: John" and "player 2: jessica"





