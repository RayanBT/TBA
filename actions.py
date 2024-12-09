# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.

from item import Item
from beamer import Beamer

# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:

    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        directions = {"NORD": "N" , "N":"N" , "SUD":"S" , "S": "S" , "OUEST":"O" , "O":"O", "EST":"E" , "E":"E" , "UP": "U" , "U":"U" , "DOWN":"D" , "D":"D"}
        # Get the direction from the list of words.
        direction = list_of_words[1]

        # Convertir la direction en majuscule
        direction = direction.upper()
        if direction in directions.keys():
            direction = directions[direction]
        
            # Move the player in the direction specified by the parameter.
            player.move(direction)
        else:
            print("La direction n'existe pas")
        return True
        

    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True
    
    def back(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de revenir à la salle précédente.

        Args:
            game (Game): L'objet du jeu.
            list_of_words (list): La liste des mots dans la commande.
            number_of_parameters (int): Le nombre de paramètres attendus par la commande.

        Returns:
            bool: True si la commande a été exécutée avec succès, False sinon.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        return game.player.back()
    
    def look(game, list_of_words, number_of_parameters):
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        return game.player.current_room.get_inventory()
    
    def history(game, list_of_words, number_of_parameters):
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        return game.player.print_history()
    
    def take(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de récupérer un item dans la salle actuelle et de le stocker dans son inventaire.

        Args:
            game (Game): L'objet du jeu.
            list_of_words (list): La liste des mots dans la commande.
            number_of_parameters (int): Le nombre de paramètres attendus par la commande.

        Returns:
            bool: True si l'item a été pris avec succès, False sinon.
        """
        # Vérifier si le nombre de paramètres est correct
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Vérifier que l'item à prendre a été spécifié
        item_name = list_of_words[1]
        current_room = game.player.current_room
        
        # Chercher l'item dans l'inventaire de la pièce actuelle
        if item_name in current_room.inventory:
            item = current_room.inventory[item_name]
            # Ajouter l'item à l'inventaire du joueur
            if game.player.add(item):
                # Retirer l'item de l'inventaire de la pièce
                current_room.inventory.pop(item_name)
                print(f"Vous avez pris {item_name}.")
                return True
            else:
                print(f"Vous ne pouvez pas prendre {item_name}, poids maximum dépassé.")
                return False
        else:
            print(f"{item_name} n'est pas dans cette pièce.")
            return False
        
    def drop(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de déposer un item de son inventaire dans la salle actuelle.

        Args:
            game (Game): L'objet du jeu.
            list_of_words (list): La liste des mots dans la commande.
            number_of_parameters (int): Le nombre de paramètres attendus par la commande.

        Returns:
            bool: True si l'item a été déposé avec succès, False sinon.
        """
        # Vérifier si le nombre de paramètres est correct
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Vérifier que l'item à déposer a été spécifié
        item_name = list_of_words[1]
        current_room = game.player.current_room
        
        # Chercher l'item dans l'inventaire du joueur
        if item_name in game.player.inventory:
            item = game.player.inventory[item_name]
            # Ajouter l'item à l'inventaire de la pièce
            current_room.inventory[item_name] = item
            # Retirer l'item de l'inventaire du joueur
            game.player.remove(item_name)
            print(f"Vous avez déposé {item_name}.")
            return True
        else:
            print(f"{item_name} n'est pas dans votre inventaire.")
            return False
        
    def check(game, list_of_words, number_of_parameters):
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        return game.player.get_inventory()
    
    def use(game, list_of_words, number_of_parameters):
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        item_name = list_of_words[1]
        item = game.player.inventory.get(item_name, None)
        
        if item_name in game.player.inventory:
            if isinstance(item, Beamer):
                return item.use(game)
        else:
            print(f"L'objet '{item_name}' n'est pas utilisable ou n'est pas un Beamer.")
            return False

    def charge(game, list_of_words, number_of_parameters):
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        item_name = list_of_words[1]
        item = game.player.inventory.get(item_name, None)
        print(item_name)
        
        if item_name in game.player.inventory:
            item.charge(game.player.current_room)
            return True
        else:
            print(f"L'objet '{item_name}' ne peut pas être chargé ou n'est pas un Beamer.")
            return False
