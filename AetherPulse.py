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

# Variables needed
    # player name, starting life total, updated life total, 
# Functions needed
    # options menu
    # Gain life, loose life
    # increment life totals (+1, +5, +10 and custom)
VERSION = "1.0.0"
    
def get_user_info(prompt):
    return input(prompt)
    # Ask user for player name
    
def get_starting_life_total(prompt):
    return input(prompt)
    # Ask user for starting life total

def player_options():
    # This will handle the user selections for various use cases
    options = int(input("Please make a selection:\n1 Gain Life\n2 Lose Life\n3 Exit program\nSelection: "))
    
    while options != 3:
        if options == 1:
            print(gaining_life())
        elif options == 2:
            print(loosing_life())
        else: 
            print("Thank you for using AetherPulse!") 

def gaining_life():
    # This will handle the options for gaining life
    life_options = int(input("Please make a selection:\n1 +1 life\n2 +5 life\n3 +10 life\nSelection: "))
    
    while life_options():
        if life_options == 1:
            
    
def loosing_life():
    # This iwll handle the options for loosing life
    
    

active_life_total = get_starting_life_total


def main():
    print("========================")
    print(f"Welcome to AetherPulse\nv{VERSION}\nThe simple to use tabletop gaming life/player tracker")
    print("========================")
    player = get_user_info("Please enter your name: ")
    player_name = player.capitalize()
    starting_life = get_starting_life_total("Please enter your current life total: ")

    print("========================")
    print(f"Game started\n{player_name} begins the game with {starting_life} life.")
    print(player_options())




if __name__ == "__main__":
    main()
    
    
            
    

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





