class Conditions:
    def __init__(self, game):
        self.game = game

    def check_victory(self):
        # Exemple de condition de victoire : le joueur doit avoir un certain objet dans son inventaire
        required_item = "bagette"
        if required_item in self.game.player.inventory:
            return f"Félicitations {self.game.player.name}, vous avez gagné en trouvant la {required_item}!"
        return None

    def check_defeat(self):
        # Exemple de condition de défaite : le joueur doit être dans une certaine pièce (par exemple, "toilette")
        defeat_room = "toilette"
        if self.game.player.current_room.name == defeat_room:
            return f"Désolé {self.game.player.name}, vous avez perdu en entrant dans la {defeat_room}."
        return None

    def check_conditions(self):
        victory_message = self.check_victory()
        if victory_message:
            self.game.finished = True
            return victory_message

        defeat_message = self.check_defeat()
        if defeat_message:
            self.game.finished = True
            return defeat_message

        return None