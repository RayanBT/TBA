"""Module contenant les fonctions appelées lorsqu'une commande est exécutée."""
# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.

#from item import Item
from beamer import Beamer

# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word
# variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:
    """
    The Actions class contains the functions that are called when a command is executed
    in the game.
    """

    @staticmethod
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
        directions = {"NORD": "N" , "N":"N" , "SUD":"S" , "S": "S" , "OUEST":"O" , "O":"O",
                       "EST":"E" , "E":"E" , "UP": "U" , "U":"U" , "DOWN":"D" , "D":"D"}
        # Get the direction from the list of words.
        direction = list_of_words[1].upper()
        if direction in directions:
            direction = directions[direction]
            # Move the player in the direction specified by the parameter.
            player.move(direction)
        else:
            print("La direction n'existe pas")
        return True

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def look(game, list_of_words, number_of_parameters):
        """
        Print the description of the current room.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            str: The description of the current room.
        
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        return game.player.current_room.get_inventory()

    @staticmethod
    def history(game, list_of_words, number_of_parameters):
        """
        Print the list of visited rooms.
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.
        Returns:
            str: The list of visited rooms.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        return game.player.print_history()

    @staticmethod
    def take(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de récupérer un item dans la salle actuelle 
        et de le stocker dans son inventaire.

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
                Actions.check_quest_item(game, item)
                return True
            print(f"Vous ne pouvez pas prendre {item_name}, poids maximum dépassé.")
            return False
        print(f"{item_name} n'est pas dans cette pièce.")
        return False

    @staticmethod
    def check_quest_item(game, item):
        """
        Vérifier si l'item récupéré fait partie de la quête actuelle.
        Args:
            game (Game): L'objet du jeu.
            item (Item): L'objet récupéré par le joueur.
        """
        # Vérifier si l'objet fait partie de la quête actuelle
        for quest in game.quests:
            current_step = quest.get_current_step()
            if current_step and current_step.item == item:
                quest.advance()
                if quest.is_complete():
                    print(f"Félicitations, vous avez complété la quête: {quest.name}")
                else:
                    print(f"Étape suivante: {current_step.description}")
                break

    @staticmethod
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
        print(f"{item_name} n'est pas dans votre inventaire.")
        return False

    @staticmethod
    def check(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de vérifier le contenu de son inventaire.
        Args:
            game (Game): L'objet du jeu.
            list_of_words (list): La liste des mots dans la commande.
            number_of_parameters (int): Le nombre de paramètres attendus par la commande.
        Returns:
            str: Le contenu de l'inventaire du joueur.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        return game.player.get_inventory()

    @staticmethod
    def use(game, list_of_words, number_of_parameters):
        """
        Permet au joueur d'utiliser un objet de son inventaire.
        Args:
            game (Game): L'objet du jeu.
            list_of_words (list): La liste des mots dans la commande.
            number_of_parameters (int): Le nombre de paramètres attendus par la commande.
        Returns:
            bool: True si l'objet a été utilisé avec succès, False sinon.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        item_name = list_of_words[1]
        item = game.player.inventory.get(item_name, None)
        if item_name in game.player.inventory:
            if isinstance(item, Beamer):
                return item.use(game)
            print(f"L'objet '{item_name}' n'est pas un Beamer.")
            return False
        print(f"L'objet '{item_name}' n'est pas dans votre inventaire.")
        return False


    @staticmethod
    def charge(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de charger un Beamer avec la salle actuelle.
        Args:
            game (Game): L'objet du jeu.
            list_of_words (list): La liste des mots dans la commande.
            number_of_parameters (int): Le nombre de paramètres attendus par la commande.
        Returns:
            bool: True si le Beamer a été chargé avec succès, False sinon.
        """
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
        print(f"L'objet '{item_name}' ne peut pas être chargé ou n'est pas un Beamer.")
        return False

    @staticmethod
    def talk(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de parler à un personnage dans la salle actuelle.
        Args:
            game (Game): L'objet du jeu.
            list_of_words (list): La liste des mots dans la commande.
            number_of_parameters (int): Le nombre de paramètres attendus par la commande.
        Returns:
            bool: True si le personnage a répondu avec succès, False sinon.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        if len(game.player.current_room.characters) >= 1:
            character_name = list_of_words[1].lower()
            character = game.player.current_room.get_character(character_name)
            if character is not None:
                if not Actions.check_quest_talk(game, character):
                    print(character.get_msg())
            else:
                print(f"Il n'y a pas de personnage nommé {character_name} dans cette pièce.")
        else:
            print("Il n'y a aucun PNJ dans cette pièce")
        return True

    @staticmethod
    def check_quest_talk(game, character):
        """
        Vérifier si le personnage avec lequel le joueur parle est lié à une quête en cours.
        Args:
            game (Game): L'objet du jeu.
            character (Character): Le personnage avec lequel le joueur parle.
        Returns:
            bool: True si la quête a avancé, False sinon.
        """
        if character is None:
            return False
        for quest in game.quests:
            current_step = quest.get_current_step()
            if current_step and current_step.character == character:
                if game.player.current_room == character.current_room:
                    Actions.handle_special_responses(current_step)
                    if Actions.handle_choices(current_step, quest):
                        Actions.advance_quest(game, quest)
                    return True
                l="Vous devez être dans la salle "
                v = " pour parler à "
                print(l + character.current_room.name + v + character.name)
                return False
        return False

    @staticmethod
    def handle_special_responses(current_step):
        """
        Gérer les réponses spéciales pour une étape de quête donnée.
        Args:
            current_step (QuestStep): L'étape de quête actuelle.
        """
        response = current_step.get_current_response()
        if response:
            print(response)

    @staticmethod
    def handle_choices(current_step, quest):
        """
        Gérer les choix pour une étape de quête donnée.
        Args:
            current_step (QuestStep): L'étape de quête actuelle.
            quest (Quest): La quête actuelle.
        Returns:
            bool: True si le joueur a fait un choix valide, False sinon.
        """
        choices = current_step.get_current_choices()
        if choices:
            for i, choice in enumerate(choices, 1):
                print(f"{i}. {choice}")
            user_choice = input("Choisissez une option: ")
            try:
                user_choice = int(user_choice)
                if 1 <= user_choice <= len(choices):
                    chosen_option = choices[user_choice - 1]
                    print(f"Vous avez choisi: {chosen_option}")
                    correct_choices = current_step.get_current_correct_choices()
                    if chosen_option in correct_choices:
                        if current_step.advance_substep():
                            return True
                        Actions.handle_special_responses(current_step)
                        return Actions.handle_choices(current_step, quest)
                    print("Choix incorrect. Vous devez recommencer l'étape.")
                    current_step.reset_substep()  # Réinitialisation de la sous-étape
                    return False
                print("Choix invalide.")
                return False
            except ValueError:
                print("Choix invalide.")
                return False
        return False

    @staticmethod
    def advance_quest(game, quest):
        """
        Faire avancer la quête actuelle.
        Args:
            game (Game): L'objet du jeu.
            quest (Quest): La quête actuelle.
        """
        current_step = quest.get_current_step()
        if current_step.advance_substep():
            quest.advance()
            if current_step.reward_item:
                game.player.inventory[current_step.reward_item.name] = current_step.reward_item
                print(f"Vous avez reçu {current_step.reward_item.name} comme récompense.")
            if quest.is_complete() and not quest.name == "La quête principale":
                print(f"Félicitations, vous avez complété la quête: {quest.name}")
            else:
                next_step = quest.get_current_step()
                if next_step:
                    next_step.current_substep = 0
                    print(f"Étape suivante: {next_step.description}")
                    if game.player.current_room == next_step.character.current_room:
                        Actions.handle_special_responses(next_step)
                        Actions.handle_choices(next_step, quest)
                    else:
                        l = "Vous devez aller dans la salle "
                        v = " pour continuer la quête."
                        print(l + next_step.character.current_room.name + v)
        else:
            Actions.handle_special_responses(current_step)
            if not Actions.handle_choices(current_step, quest):
                print("Vous avez échoué cette étape de la quête. Veuillez réessayer.")
