"""This module defines the Room class, which represents a room in the game world."""
# Define the Room class.

class Room:
    """This class represents a room in the game world."""
    # Define the constructor.
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = {}
        self.characters = {}

    # Define the get_exit method.
    def get_exit(self, direction):
        """
        Return the room in the given direction if it exists.
        Args:
            direction (str): The direction in which to get the room.
        Returns:
            Room: The room in the given direction if it exists, None otherwise.
        """
        # Return the room in the given direction if it exists.
        return self.exits.get(direction, None)

    # Return a string describing the room's exits.
    def get_exit_string(self):
        """
        Return a string describing the room's exits.
        Returns:
            str: A string describing the room's exits.
        """
        exit_string = "Sorties: "
        for exit in self.exits:
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        """
        Return a long description of this room including exits.
        Returns:
            str: A long description of this room including exits.
        """
        return f"\nVous êtes dans {self.description}\n\n{self.get_exit_string()}\n"

    def get_inventory(self):
        """
        Return the inventory of the room.
        Returns:
            dict: The inventory of the room.
        """
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

    def get_character(self, name):
        """
        Return the character in the room with the given name.
        Args:
            name (str): The name of the character to return.
        Returns:
            Character: The character in the room with the given name.
        """
        name_lower = name.lower()
        for key, character in self.characters.items():  # Utilisation de .items()
            if key.lower() == name_lower:
                return character
        return None
