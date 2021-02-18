# Write a class to hold player information, e.g. what room they are in
# currently.

class Player: 
    def __init__(self, name, current_room):
        self.name = name 
        self.current_room = current_room
        self.inventory = []  

# a class is created called Player
# Function inside class called __init__
# each attribute is defined by its parameter
# inventory is an empty array because it contains what the player has 