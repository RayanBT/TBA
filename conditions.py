""" Module contenant les conditions de victoire et de défaite du jeu. """
import time
from config import DEBUG

class Conditions:
    """ Classe représentant les conditions de victoire et de défaite du jeu. """
    def __init__(self, game):
        self.game = game

    def check_victory(self, required_items, all_required=True):
        """
        Vérifie si le joueur a gagné en trouvant tous les objets requis.
        Args:
            required_items (list): Liste des objets requis pour gagner.
            all_required (bool): True si tous les objets sont requis, False si un seul suffit.
        Returns:
            bool: True si le joueur a gagné, False sinon.
        """
        if all_required:
            # Vérifier si tous les objets requis sont dans l'inventaire
            if DEBUG:
                print(f"Inventaire du joueur : {self.game.player.inventory.keys()}")
                print(f"all: {all(item in self.game.player.inventory.keys()
                                  for item in required_items)}")
            if all(item in self.game.player.inventory for item in required_items):
                messages = [
                    f"Félicitations {self.game.player.name}, vous avez gagné en trouvant tous les objets requis!",
                    "Vous avez accompli toutes les quêtes.",
                    "Votre aventure à Poudlard est un succès.",
                    "À bientôt pour de nouvelles aventures !",
                    "À l'année prochaine !",
                    "Merci d'avoir joué!"
                ]
                print_with_delay(messages)
                self.game.finished = True
                return True
        else:
            # Vérifier si au moins un des objets requis est dans l'inventaire
            if any(item in self.game.player.inventory for item in required_items):
                messages = [
                    f"Félicitations {self.game.player.name}, vous avez gagné en trouvant au moins un des objets requis!",
                    "Votre aventure continue avec succès.",
                    "Merci d'avoir joué!"
                ]
                print_with_delay(messages)
                self.game.finished = True
                return "Victoire"
        return None

    def check_defeat(self):
        """
        Vérifie si le joueur a perdu en entrant dans une salle spécifique.
        Returns:
            bool: True si le joueur a perdu, False sinon.
        """
        defeat_room = "salle_sombre"
        if self.game.player.current_room.name == defeat_room:
            messages = [
                f"Désolé {self.game.player.name}, vous avez perdu en entrant dans la {defeat_room}.",
                "Vous sentez une présence maléfique autour de vous.",
                "Votre vision commence à se brouiller.",
                "Vous entendez des murmures inquiétants.",
                "Vous avez perdu conscience..."
            ]
            print_with_delay(messages)
            #self.game.finished = True  # Marquer le jeu comme terminé
            return True
        return None

    def check_conditions(self, required_items, all_required=True):
        """
        Vérifie les conditions de victoire et de défaite du jeu.
        Args:
            required_items (list): Liste des objets requis pour gagner.
            all_required (bool): True si tous les objets sont requis, False si un seul suffit.
        Returns:
            str: Message de victoire ou de défaite, None sinon.
        """
        victory_message = self.check_victory(required_items, all_required)
        if victory_message:
            self.game.finished = True
            return victory_message

        defeat_message = self.check_defeat()
        if defeat_message:
            self.game.finished = True
            return defeat_message

        return None

def print_with_delay(messages, delay=1.0):
    """ 
    Affiche une liste de messages avec un délai entre chaque message.
    Args:
        messages (list): Liste des messages à afficher.
        delay (float): Délai entre chaque message.
    """
    for message in messages:
        print(message)
        time.sleep(delay)
