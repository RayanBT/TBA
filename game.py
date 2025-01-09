# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from beamer import Beamer
from character import Character
from config import DEBUG
from conditions import Conditions
from quest import Quest, QuestStep


class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.conditions = None
        self.quests = []
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        back_cmd = Command("back", " : revenir à la salle précédente", Actions.back, 0)
        self.commands["back"] = back_cmd
        look = Command("look", " : regarder les objets dans la pièce", Actions.look, 0)
        self.commands["look"] = look
        take = Command("take", " : prendre un objet", Actions.take, 1)
        self.commands["take"] = take
        drop = Command("drop", " : lâcher un objet", Actions.drop, 1)
        self.commands["drop"] = drop
        history = Command("history", " : affiche l'historique des salles", Actions.history, 0)
        self.commands["history"] = history
        check = Command("check", " : affiche l'inventaire du joueur", Actions.check, 0)
        self.commands["check"] = check
        use = Command("use", " : utilise un item de ton inventaire", Actions.use, 1)
        self.commands["use"] = use
        charge = Command("charge", " : charger un Beamer avec la salle actuelle", Actions.charge, 1)
        self.commands["charge"] = charge
        talk = Command("talk", " : interagir avec un pnj de la meme piece", Actions.talk, 1)
        self.commands["talk"] = talk

        # Setup rooms

        entrée = Room("entrée", "le couloire principale de l'ecole de poudlard.")
        self.rooms.append(entrée)
        depot_affaire = Room("dépôt affaire", "la pièce remplie d'affaires d'étudiants de l'école.")
        self.rooms.append(depot_affaire)
        jardin = Room("jardin", "un jardin, au milieu, il y a une fontaine avec des plantes qui chantent.")
        self.rooms.append(jardin)
        cours_botanique = Room("cours_botanique", "une serre entourée de plantes magiques.")
        self.rooms.append(cours_botanique)
        couloir_etage_1 = Room("couloir_etage_1", "le couloire de l'étage 1.")
        self.rooms.append(couloir_etage_1)
        salle_commune_de_Gryffondor = Room("salle_commune_de_Gryffondor", "la salle commune de Gryffondor, cette salle est remplie de rouge, avec principalement du bois comme matériau.")
        self.rooms.append(salle_commune_de_Gryffondor)
        cours_de_magie = Room("cours_de_magie", "une salle de classe avec plusieurs rangées de tables et une céramique de dinosaure au plafond.")
        self.rooms.append(cours_de_magie)
        salle_commune = Room("salle_commune", "une grande salle avec plusieurs tables de banquet, tout au bout de la salle il y a la table des professeurs, des bougies flottant au plafond.")
        self.rooms.append(salle_commune)
        couloir_etage_2 = Room("couloir_etage_2", "le couloir de l'étage 2, très large rempli de fenêtres avec une vue incontournable.")
        self.rooms.append(couloir_etage_2)
        cours_potion = Room("cours_potion", "une salle sombre avec plusieurs paillasses, possédant une marmite et des produits que vous ne connaissez pas.")
        self.rooms.append(cours_potion)
        salle_commune_Serpentard = Room("salle_commune_Serpentard", "une salle avec un aquarium, des canapés en cuir et à l'étage vos lits aux couleurs du blason.")
        self.rooms.append(salle_commune_Serpentard)
        toilette = Room("toilette", "une salle avec des robinets en plein milieu et un peu d'eau au sol.")
        self.rooms.append(toilette)
        cours_animaux_magiques = Room("cours_animaux_magiques", "une salle plusieurs animaux en cage, et des squelettes autour de la salle.")
        self.rooms.append(cours_animaux_magiques)
        couloir_etage_3 = Room("couloir_etage_3", "le vouloire de l'étage 3, une tour avec un couloir très fin.")
        self.rooms.append(couloir_etage_3)
        salle_commune_de_Poufsouffle = Room("salle_commune_de_Poufsouffle", "une pièce ovale avec plusieurs étagères remplies de livres.")
        self.rooms.append(salle_commune_de_Poufsouffle)
        salle_commune_de_Serdaigle = Room("salle_commune_de_Serdaigle", "une très épurée, très claire et remplie de fenêtres qui laissent entrer la lumière du jour.")
        self.rooms.append(salle_commune_de_Serdaigle)
        cours_de_defance = Room("cours_de_defance", "une salle possédant un pupitre d'affrontement de sorciers et des chaises.")
        self.rooms.append(cours_de_defance)


        # Create exits for rooms

        entrée.exits = {"N" : None, "E" : None, "S" : depot_affaire, "O" : jardin ,"U" : couloir_etage_1 , "D" : None}
        depot_affaire.exits = {"N" : entrée, "E" : None, "S" : None, "O" : None ,"U" : couloir_etage_1 , "D" : None}
        jardin.exits = {"N" : cours_botanique, "E" : entrée, "S" : None, "O" : None ,"U" : couloir_etage_1 , "D" : None}
        cours_botanique.exits = {"N" : None, "E" : None, "S" : jardin, "O" : None ,"U" : couloir_etage_1 , "D" : None}
        couloir_etage_1.exits = {"N" : salle_commune_de_Gryffondor, "E" : cours_de_magie, "S" : salle_commune, "O" : None ,"U" : couloir_etage_2 , "D" : entrée}
        salle_commune_de_Gryffondor.exits = {"N" : None, "E" : None, "S" : couloir_etage_1, "O" : None ,"U" : couloir_etage_2 , "D" : entrée}
        cours_de_magie.exits = {"N" : None, "E" : None, "S" : None, "O" : couloir_etage_1 ,"U" : couloir_etage_2 , "D" : entrée}
        salle_commune.exits = {"N" : couloir_etage_1, "E" : None, "S" : None, "O" : None ,"U" : couloir_etage_2 , "D" : entrée}
        couloir_etage_2.exits = {"N" : cours_potion, "E" : salle_commune_Serpentard, "S" : toilette, "O" : cours_animaux_magiques ,"U" : couloir_etage_3 , "D" : couloir_etage_1}
        cours_potion.exits = {"N" : None, "E" : None, "S" : couloir_etage_2, "O" : None ,"U" : couloir_etage_3 , "D" : couloir_etage_1}
        salle_commune_Serpentard.exits = {"N" : None, "E" : None, "S" : None, "O" : couloir_etage_2 ,"U" : couloir_etage_3 , "D" : couloir_etage_1}
        cours_animaux_magiques.exits = {"N" : None, "E" : couloir_etage_2, "S" : None, "O" : None ,"U" : couloir_etage_3 , "D" : couloir_etage_1}
        toilette.exits = {"N" : couloir_etage_2, "E" : None, "S" : None, "O" : None ,"U" : couloir_etage_3 , "D" : couloir_etage_1}
        couloir_etage_3.exits = {"N" : salle_commune_de_Poufsouffle, "E" : salle_commune_de_Serdaigle, "S" : cours_de_defance, "O" : None ,"U" : None , "D" : couloir_etage_2}
        salle_commune_de_Poufsouffle.exits = {"N" : None, "E" : None, "S" : couloir_etage_3, "O" : None ,"U" : None , "D" : couloir_etage_2}
        salle_commune_de_Serdaigle.exits = {"N" : None, "E" : None, "S" : None, "O" : couloir_etage_3 ,"U" : None , "D" : couloir_etage_2}
        cours_de_defance.exits = {"N" : couloir_etage_3, "E" : None, "S" : None, "O" : None ,"U" : None , "D" : couloir_etage_2}

        # Setup items

        bagette = Item("bagette", "une bagette magique en ecaille de dragon", 30)
        depot_affaire.inventory[bagette.name] = bagette
        cape = Item("cape", "une longue cape noir", 50)
        depot_affaire.inventory[cape.name] = cape
        chapeau = Item("chapeau", "un chapeau pointuelégèrement abimé", 60)
        depot_affaire.inventory[chapeau.name] = chapeau
        beamer = Beamer("beamer", "Un appareil magique pour téléporter.", 25)
        toilette.inventory[beamer.name] = beamer

        # Setup characters (PNJ)
        
        gandalf = Character("gandalf", "un magicien blanc", entrée, ["Abracadabra !"])
        entrée.characters[gandalf.name] = gandalf
        hermione = Character("Hermione", "une sorcière très intelligente", salle_commune_de_Gryffondor, ["Bonjour, je suis Hermione."])
        salle_commune_de_Gryffondor.characters[hermione.name] = hermione

        dumbledore = Character("Dumbledore", "le directeur de l'école", salle_commune, ["Bienvenue à Poudlard !"])
        salle_commune.characters[dumbledore.name] = dumbledore

        hagrid = Character("Hagrid", "le gardien des clés et des lieux", jardin, ["Salut, je suis Hagrid."])
        jardin.characters[hagrid.name] = hagrid

        snape = Character("Snape", "le professeur de potions", cours_potion, ["Je suis le professeur Snape."])
        cours_potion.characters[snape.name] = snape
        
        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = entrée

        # Setup conditions
        self.conditions = Conditions(self)

        # Setup quests
        quest_steps = [
            QuestStep("Parlez à Hermione dans la salle commune de Gryffondor.", character=hermione),
            QuestStep("Parlez à Dumbledore dans la salle commune.", character=dumbledore),
            QuestStep("Parlez à Hagrid dans le jardin.", character=hagrid),
            QuestStep("Parlez à Snape dans le cours de potions.", character=snape),
            QuestStep("Récupérez la bagette magique.", item=bagette)
        ]
        main_quest = Quest("La quête principale", "Accomplissez les tâches pour avancer dans l'histoire.", quest_steps)
        self.quests.append(main_quest)

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
            end_message = self.conditions.check_conditions()
            if end_message:
                print(end_message)
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:
        # Split the command string into a list of words
        list_of_words = command_string.split(" ")
        command_word = list_of_words[0]
        if command_word != "":
            # If the command is not recognized, print an error message
            if command_word not in self.commands.keys():
                print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
            # If the command is recognized, execute it
            else:
                command = self.commands[command_word]
                command.action(self, list_of_words, command.number_of_parameters)
                if command_word != "quit":
                    #self.move_characters()
                    pass

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        print(self.player.current_room.get_long_description())

         # Informer le joueur de la première étape de la quête
        if self.quests:
            first_quest = self.quests[0]
            first_step = first_quest.get_current_step()
            if first_step:
                print(f"\nQuête actuelle: {first_quest.name}")
                print(f"Étape actuelle: {first_step.description}")

    def move_characters(self):
        for room in self.rooms:
            # Créer une copie de la liste des personnages dans la pièce
            characters_to_move = list(room.characters.values())  # Liste des personnages à déplacer
            for character in characters_to_move:
                character.move()

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
