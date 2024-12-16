# Define the Room class.

class Room:

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = {}
        self.characters = {}
    
    # Define the get_exit method.
    def get_exit(self, direction):
        # Return the room in the given direction if it exists.
        return self.exits.get(direction, None)
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes dans {self.description}\n\n{self.get_exit_string()}\n"
    
    def get_inventory(self):
        if len(self.inventory) >= 1 or len(self.characters) >= 1:
            print("\nOn voit :")
            if len(self.inventory) >= 1:
                for name, item in self.inventory.items():
                    print(f"    - {name} : {item.description} ({item.weight} g)")
            elif len(self.characters) >= 1:
                for name, item in self.characters.items():
                    print(f"    - {item}")
            else:
                print("pas de PNJ")
        else:
            print("\nIl n'y a rien ici.")
    
    

