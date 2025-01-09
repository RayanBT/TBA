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
        salle_sombre = Room("salle_sombre", "une salle sombre avec plusieur cadavre d'etudiant.")
        self.rooms.append(salle_sombre)

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
        salle_sombre.exits = {"N" : couloir_etage_3, "E" : None, "S" : None, "O" : None ,"U" : None , "D" : couloir_etage_2}#a faire ---------------------------------

        # Setup items

        bagette = Item("bagette", "une bagette magique en ecaille de dragon", 30)
        depot_affaire.inventory[bagette.name] = bagette
        cape = Item("cape", "une longue cape noir", 50)
        depot_affaire.inventory[cape.name] = cape
        chapeau = Item("chapeau", "un chapeau pointuelégèrement abimé", 60)
        depot_affaire.inventory[chapeau.name] = chapeau
        beamer = Beamer("beamer", "Un appareil magique pour téléporter.", 25)
        toilette.inventory[beamer.name] = beamer
        livre = Item("livre", "un livre de sorts", 10)
        potion = Item("potion", "une potion de guérison", 5)
        cape_sombre = Item("cape", "une cape noir avec des motif plus sombre", 5)
        diplome_de_magie = Item("diplome de magie", "un diplome de magie", 1)
        diplome_de_botanique = Item("diplome de botanique", "un diplome de botanique", 1)
        diplome_de_potion = Item("diplome de potion", "un diplome de potion", 1)
        diplome_d_annimeaux_magique = Item("diplome d'annimeaux magique", "un diplome d'annimeaux magique", 1)
        diplome_de_defance = Item("diplome de defance", "un diplome de defance", 1)
        

        # Setup characters (PNJ)
        chapeau_magique = Character("chapeau magique", "un chapeau sombre et abimer pouvant parler", salle_commune, ["Bonjour, je suis un chapeau magique."])
        salle_commune.characters[chapeau_magique.name] = chapeau_magique

        dumbledore = Character("Dumbledore", "le directeur de l'école", salle_commune, ["Bienvenue à Poudlard !"])
        salle_commune.characters[dumbledore.name] = dumbledore

        hagrid = Character("Hagrid", "le gardien des clés et des lieux", jardin, ["Salut, je suis Hagrid."])
        jardin.characters[hagrid.name] = hagrid

        professeur_de_magie = Character("professeur_de_magie", "le professeur de magie avec un tres large chapeaux", cours_de_magie, ["Je suis le professeur de magie."])
        cours_de_magie.characters[professeur_de_magie.name] = professeur_de_magie

        professeur_des_annimeaux_magique = Character("professeur_des_annimeaux_magique", "le professeur des annimeaux avec un manteaux vert", cours_animaux_magiques, ["Je suis le professeur des annimeaux magie."])
        cours_animaux_magiques.characters[professeur_des_annimeaux_magique.name] = professeur_des_annimeaux_magique
        
        professeur_de_botanique = Character("professeur_de_botanique", "le professeur de botanique avec des gant", professeur_de_botanique, ["Je suis le professeur de botanique."])
        cours_animaux_magiques.characters[professeur_de_botanique.name] = professeur_de_botanique

        professeur_de_potion = Character("professeur_de_potion", "le professeur de potion avec une longue cape sombre", professeur_de_potion, ["Je suis le professeur de potion."])
        cours_animaux_magiques.characters[professeur_de_potion.name] = professeur_de_potion
        
        professeur_de_defance = Character("professeur_de_defance", "le professeur de defance avec un ", professeur_de_defance, ["Je suis le professeur de defance."])
        cours_animaux_magiques.characters[professeur_de_defance.name] = professeur_de_defance
        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = entrée

        # Setup conditions
        self.conditions = Conditions(self)

        # Setup quests
        quest_steps = [
            QuestStep(
                "Parlez au chpeau dans la salle commune.",
                character=chapeau_magique,
                special_responses=[
                    "chapeau magique : Bonjour, je suis ici pour que vous choisisait votre maison",
                    "chapeau magique : quelle maison vouslez vous ?"
                ],
                choices=[
                    ["Oui, je veux choisir.", "Non, je suis occupé."],
                    ["Gryffondor","Serpentard","Serdaigle","Poufsouffle"]
                ],
                correct_choices=[["Oui, je veux choisir."],[]], #plusieur corect choix-----------------------------------------------------
                reward_item=cape_sombre
            ),
            QuestStep(
                "assister au cour de magie dans la salle de magie",
                character=professeur_de_magie,
                special_responses=[
                    "professeur de magie : Bienvenue à Poudlard ! Êtes-vous prêt à apprendre un sort ?",
                    "professeur de magie : Répétez après moi : 'Accio'.",
                    "professeur de magie : Répétez après moi : 'Lumos'.",
                    "professeur de magie : Répétez après moi : 'Alohomora'."
                ],
                choices=[
                    ["Oui, je suis prêt.", "Non, pas maintenant."],
                    ["Acioo", "Accio", "Accie"],
                    ["Lumos", "Lumo", "Lmos"],
                    ["Alohoomoa", "Alohmiora", "Alohomora"]
                ],
                correct_choices=[
                    ["Oui, je suis prêt."],
                    ["Accio"],
                    ["Lumos"],
                    ["Alohomora"]
                ],
                reward_item=diplome_de_magie
            ),
            QuestStep(
                "assister au cour de botanique dans la salle de botanique",
                character=professeur_de_botanique,
                special_responses=[
                    "professeur de botanique : Bienvenue à Poudlard ! Êtes-vous prêt à apprendre un sort ?",
                    "professeur de botanique : pour faire replanter une mandragore il faut l'arracher d'un coup sec en mettant vos bouchon d'oreil",
                    "professeur de botanique : il faut la placer dans le nouveau pot et remborée avec de la terre"
                ],
                choices=[
                    ["Oui, je suis prêt.", "Non, pas maintenant."],
                    ["arracher la plante", "mettre ses bouchon d'oreil et arracher la plante", "mettre ses bouchon d'oreil"],
                    ["mettre la mandragore dans un pot et rajouter du fumier", "mettre la mandragore dans un pot", "mettre de la terre dans le pot"]
                ],
                correct_choices=[
                    ["Oui, je suis prêt."],
                    ["mettre ses bouchon d'oreil et arracher la plante"],
                    ["mettre la mandragore dans un pot et rajouter du fumier"]
                ],
                reward_item=diplome_de_botanique
            ),
            QuestStep(
                "assister au cour de potion dans la salle de potion",
                character=professeur_de_potion,
                special_responses=[
                    "professeur de potion : Bienvenue à Poudlard ! Êtes-vous prêt à apprendre un sort ?",
                    "professeur de potion : pour faire Felix Felicis mettre des crocher d'aregnier",
                    "professeur de potion : il faut apresant des feuille de mandragore"
                ],
                choices=[
                    ["Oui, je suis prêt.", "Non, pas maintenant."],
                    ["mettre de l'eau", "mettre des crocher d'aregnier", "mettre du jus de citrouille"],
                    ["mettre des feuille de mandragore", "mettre une plume de hibou", "mettre du radi venimeux"]
                ],
                correct_choices=[
                    ["Oui, je suis prêt."],
                    ["mettre des crocher d'aregnier"],
                    ["mettre des feuille de mandragore"]
                ],
                reward_item=diplome_de_potion
            ),
            QuestStep(
                "assister au cour de annimaux magique",
                character=professeur_des_annimeaux_magique,
                special_responses=[
                    "professeur des annimeaux magique : Bienvenue à Poudlard ! Êtes-vous prêt à apprendre un sort ?",
                    "professeur des annimeaux magique : repéré un annimal magique ressanblant a un cheval mais avec une corne sur la tete",
                ],
                choices=[
                    ["Oui, je suis prêt.", "Non, pas maintenant."],
                    ["un hippogriffe", "une licorne", "un Phénix"]
                ],
                correct_choices=[
                    ["Oui, je suis prêt."],
                    ["une licorne"]
                ],
                reward_item=diplome_d_annimeaux_magique
            ),
            QuestStep(
                "assister au cour de defance dans la salle de defance",
                character=professeur_de_defance,
                special_responses=[
                    "professeur de defance : Bienvenue à Poudlard ! Êtes-vous prêt à apprendre un sort ?",
                    "professeur de defance : Répétez après moi : 'Stupéfix'.",
                    "professeur de defance : Répétez après moi : 'Protego'.",
                    "professeur de defance : Répétez après moi : 'Petrificus Totalus'."
                ],
                choices=[
                    ["Oui, je suis prêt.", "Non, pas maintenant."],
                    ["Stuqéfix", "Stupéfix", "Stipéfix"],
                    ["Protego", "Proteqo", "Prottego"],
                    ["Petrificus Totalus", "Petrificus Totalu", "Pettrificus Totalus"]
                ],
                correct_choices=[
                    ["Oui, je suis prêt."],
                    ["Stupéfix"],
                    ["Protego"],
                    ["Petrificus Totalus"]
                ],
                reward_item=diplome_de_defance
            ),
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
