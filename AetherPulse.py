# !/usr/bin/env python3

"""
AetherPulse
Tabletop Game Life/Player Tracker
---------------------------------
This program runs in the command 
line and allows players to maintain 
life totals of one or more users. 
---------------------------------
Usage:
    coming soon
    
Author: Christian Ventura
Date: 2025-08-10
---------------------------------
Returns:
    _type_: _description_
"""

print("========================")
print("Welcome to AetherPulse\nThe simple to use Magic the Gathering life tracker")
print("========================")
player_one = input("Please enter your name: ")
player_name = player_one.capitalize()
starting_life_total = int(input("Please enter your current life total: "))

print("========================")
print(f"Match started\n{player_name} begins the game with {starting_life_total} life.")

# Variables needed
    # player name, starting life total, updated life total, 
# Functions needed
    # options menu
    # Gain life, loose life
    # increment life totals (+1, +5, +10 and custom)


def player_options():
    options = int(input("Please make a selection:\n1 Gain Life\n2 Lose Life\n3 Exit program\nSelection: "))
    
    while options != 3:
        if options == 1:
            gain_life_options()
            # gained_life = input("How much life is gained? ")
            # new_life_total = starting_life_total + gained_life
            # print(f"{player_name} now has {current_life_total} life.") 
            # return player_options()
        # THIS IS WHERE I LEFT OFF!!
        # Continue figuring out how to store the new, updated life totals after each change occurs
        elif options == 2:
            lose_life_options()
            # life_lost = input("How much life is lost? ")
            # print(f"{player_name} now has {current_life_total} life.")
            # return player_options()

    return "Thank you for using AetherPulse!"

print(player_options())

def gain_life_options():
    gain_options = int(input("How much life is gained?\n1 Gain +1 life\n2 Gain +5 life\n3 Gain +10 life\n4 Gain custom amount of life\nSelection: "))
    if gain_options == 1:
        
            

def lose_life_options():
    loss_options = int(input("How much life is lost?\n1 Loose +1 life\n2 Loose +5 life\n3 Loose +10 life\n4 Loose a custom amount of life\nSelection: "))
    
    
    
    
            
    

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





