""" Module contenant la classe Beamer. """

from item import Item

class Beamer(Item):
    """ Classe représentant un Beamer. """
    def __init__(self, name, description, weight, teleport_room=None):
        super().__init__(name, description, weight)
        self.teleport_room = teleport_room  # La salle où le Beamer peut téléporter

    def use(self, game):
        """
        Utiliser le Beamer pour téléporter le joueur.
        Args:
            game (Game): L'instance du jeu.
        Returns:
            bool: True si le Beamer a été utilisé, False
        """
        if self.teleport_room:
            print(f"Vous êtes téléporté dans la salle : {self.teleport_room.name}.")
            game.player.current_room = self.teleport_room
            game.player.history.append(game.player.current_room)
            print(game.player.current_room.get_long_description())
            game.player.print_history()
            return True
        print("Le Beamer n'est pas chargé avec une destination.")
        return False

    def charge(self, current_room):
        """
        Charger le Beamer avec la salle actuelle.
        Args:
            current_room (Room): La salle actuelle.
        """
        self.teleport_room = current_room
        print(f"Le Beamer est maintenant chargé avec la salle : {current_room.name}.")
