"""Module contenant la classe Inventory."""

class Inventory:
    """Classe représentant l'inventaire du joueur."""
    def __init__(self) -> None:
        self.inventory = {}
        self.poid = 0
        self.max_weight = 5000

    def add(self, item):
        """
        Ajoute un objet à l'inventaire.
        Args:
            item (Item): L'objet à ajouter.
        Returns:
            bool: True si l'objet a été ajouté, False sinon.
        """
        if self.poid + item.weight <= self.max_weight:
            self.inventory[item.name] = item
            self.poid += item.weight
            print(f"{item.name} a été ajouté à l'inventaire.")
            return True
        print(f"Vous ne pouvez pas ajouter {item.name}, poids maximum dépassé.")
        return False

    def remove(self, item_name):
        """
        Retire un objet de l'inventaire.
        Args:
            item_name (str): Le nom de l'objet à retirer.
        """
        if item_name in self.inventory:
            item = self.inventory.pop(item_name)
            self.poid -= item.weight
            print(f"{item_name} a été retiré de l'inventaire.")
        else:
            print(f"{item_name} n'est pas dans l'inventaire.")

    def get_inventory(self):
        """
        Retourne l'inventaire du joueur.
        Returns:
            dict: L'inventaire du joueur.
        """
        if len(self.inventory) > 0:
            print("\nInventaire :")
            for name, item in self.inventory.items():
                print(f"    - {name} : {item.description} ({item.weight} g)")
        else:
            print("\nL'inventaire est vide.")
