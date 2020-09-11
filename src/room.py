# Implement a class to hold room information. This should have name and
# description attributes.
class Room: 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.s_to = ""
        self.n_to = ""
        self.w_to = ""
        self.e_to = ""
        self.item_list = []
# Class is named Room and it contains a function called __init__
# each attritbute is defined by their parameters
# direction attributes are empty strings because it contains each item the room has
# item_list is an empty array because it contains a set of items the room has