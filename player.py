# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
    
    # Define the move method.
    def move(self, direction):
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
            print("\nErreur : La salle actuelle n'a pas de sorties ou la direction n'est pas valide.")
            return False
        except Exception as e:
            print(f"\nUne erreur inattendue s'est produite : {e}")
            return False

    # Retoure les lieux visités
    def print_history(self):
        try:
            if len(self.history) >= 1:
                print("\nVous avez déjà visité les pièces suivantes:")
                for room in self.history:  # Exclut la pièce actuelle de l'historique affiché
                    print(f"    - {room.description}")
            else:
                print("\nVous n'avez visité aucune autre pièce.")
        except Exception as e:
            print(f"\nUne erreur inattendue s'est produite lors de l'affichage de l'historique : {e}")

    # Define the back method.
    def back(self):
        try:
            if len(self.history) >= 1:
                # Set the current room to the previous room
                self.current_room = self.history.pop()
                print(self.current_room.get_long_description())
                self.print_history()
                return True
            else:
                print(self.history)
                print("\nVous ne pouvez pas revenir en arrière !\n")
                return False
        except Exception as e:
            print(f"\nUne erreur inattendue s'est produite lors du retour en arrière : {e}")
            return False