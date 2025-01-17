"""This module defines the Player class."""
from inventory import Inventory
from config import DEBUG

# Define the Player class.
class Player(Inventory):
    """This class represents a player in the game."""
    # Define the constructor.
    def __init__(self, name, current_room = None):
        super().__init__()
        self.name = name
        self.current_room = current_room
        self.history = []

    # Define the move method.
    def move(self, direction):
        """
        Move the player in the given direction.
        Args:
            direction (str): The direction in which to move.
        Returns:
            bool: True if the player moved successfully, False otherwise.
        """
        try:
            # Convertir la direction en majuscule
            direction = direction.upper()
            # Vérifie que la salle actuelle et la direction sont valides.
            if not self.current_room or direction not in self.current_room.exits:
                print("\nAucune porte dans cette direction !\n")
                return False
            # Obtient la prochaine salle et vérifie qu'elle n'est pas None.
            next_room = self.current_room.exits[direction]
            if next_room is None:
                print("\nAucune porte dans cette direction !\n")
                return False
            # Change la salle actuelle pour la suivante.
            self.current_room = next_room
            self.history.append(next_room)
            print(self.current_room.get_long_description())
            self.print_history()
            return True
        except AttributeError:
            if DEBUG:
                print("\nErreur : La salle actuelle n'a pas de sorties ou la direction n'est pas valide.")
                return False
        except Exception as e:
            if DEBUG:
                print(f"\nUne erreur inattendue s'est produite : {e}")
                return False

    # Retoure les lieux visités
    def print_history(self):
        """ Print the history of visited rooms. """
        try:
            if len(self.history) > 1:
                print("\nVous avez déjà visité les pièces suivantes:")
                for room in self.history[:-1]:  # Exclut la pièce actuelle de l'historique affiché
                    print(f"    - {room.description}")
            else:
                print("\nVous n'avez visité aucune autre pièce.")
        except Exception as e:
            print(f"\nUne erreur inattendue s'est produite lors de l'affichage de l'historique : {e}")

    # Define the back method.
    def back(self):
        """ Move the player back to the previous room. """
        try:
            if len(self.history) > 1:
                self.history.pop()
                self.current_room = self.history[-1]
                print(self.current_room.get_long_description())
                self.print_history()
                return True
            print("\nVous ne pouvez pas revenir en arrière !\n")
            return False
        except Exception as e:
            print(f"\nUne erreur inattendue s'est produite lors du retour en arrière : {e}")
            return False
