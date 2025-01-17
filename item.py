""" Item class for the game """
class Item() :
    """ Class representing an item in the game """
    def __init__(self, name, description, weight):
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self) :
        """ Returns a string representation of the item """
        return f"{self.name} : {self.description} ({self.weight} g)"
