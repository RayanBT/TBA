""" Game class for the text-based adventure game. """
# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from beamer import Beamer
from character import Character
from conditions import Conditions
from quest import Quest, QuestStep


class Game:
    """ Game class for the text-based adventure game. """

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
        """ Setup the game. """

        # Setup commands
        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O, U, D)",
                    Actions.go, 1)
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
        entree = Room("entree", "le couloir principal de l'école de Poudlard.")
        self.rooms.append(entree)
        depot_affaire = Room("dépôt_affaire",
                            "une pièce remplie d'affaires d'étudiants de l'école.")
        self.rooms.append(depot_affaire)
        jardin = Room("jardin",
                    ("un jardin où, au milieu, se trouve"
                     " une fontaine entourée de plantes qui chantent."))
        self.rooms.append(jardin)
        cours_botanique = Room("cours_botanique", "une serre remplie de plantes magiques.")
        self.rooms.append(cours_botanique)
        couloir_etage_1 = Room("couloir_etage_1", "le couloir du premier étage.")
        self.rooms.append(couloir_etage_1)
        salle_commune_de_gryffondor = Room("salle_commune_de_gryffondor",
                                        ("la salle commune de Gryffondor,"
                                         " décorée en rouge avec du bois en abondance."))
        self.rooms.append(salle_commune_de_gryffondor)
        cours_de_magie = Room("cours_de_magie",
                            ("une salle de classe avec plusieurs rangées"
                             " de tables et une maquette de dinosaure suspendue au plafond."))
        self.rooms.append(cours_de_magie)
        salle_commune = Room("salle_commune",
                            ("une grande salle avec plusieurs tables de"
                             " banquet et des bougies flottant au plafond."))
        self.rooms.append(salle_commune)
        couloir_etage_2 = Room("couloir_etage_2",
                            ("le couloir du deuxième étage, large et "
                             "rempli de fenêtres offrant une vue imprenable."))
        self.rooms.append(couloir_etage_2)
        cours_potion = Room("cours_potion",
                            ("une salle sombre avec plusieurs paillasses,"
                             " une marmite, et des ingrédients étranges."))
        self.rooms.append(cours_potion)
        salle_commune_serpentard = Room("salle_commune_serpentard",
                                    ("une salle avec un grand aquarium, des canapés"
                                     " en cuir, et des lits aux couleurs de Serpentard."))
        self.rooms.append(salle_commune_serpentard)
        toilette = Room("toilette",
                        ("une salle avec des robinets alignés au "
                         "centre et de l'eau qui coule légèrement au sol."))
        self.rooms.append(toilette)
        cours_animaux_magiques = Room("cours_animaux_magiques",
                                    ("une salle remplie de cages contenant "
                                     "des animaux et de squelettes exposés."))
        self.rooms.append(cours_animaux_magiques)
        couloir_etage_3 = Room("couloir_etage_3",
                               "le couloir du troisième étage, étroit et serpentant dans une tour.")
        self.rooms.append(couloir_etage_3)
        salle_commune_de_poufsouffle = Room("salle_commune_de_poufsouffle",
                                            ("une pièce ovale avec de nombreuses"
                                             " étagères remplies de livres."))
        self.rooms.append(salle_commune_de_poufsouffle)
        salle_commune_de_serdaigle = Room("salle_commune_de_serdaigle",
                                          ("une salle lumineuse et épurée, remplie de "
                                           "fenêtres laissant entrer la lumière du jour."))
        self.rooms.append(salle_commune_de_serdaigle)
        cours_de_defense = Room("cours_de_defense",
                                ("une salle avec un pupitre pour les duels "
                                 "et des chaises disposées en demi-cercle."))
        self.rooms.append(cours_de_defense)
        salle_sombre = Room("salle_sombre",
                            "une salle lugubre avec plusieurs cadavres d'étudiants abandonnés.")
        self.rooms.append(salle_sombre)

        # Create exits for rooms
        entree.exits = {"N": None, "E": None, "S": depot_affaire, "O": jardin,
                        "U": couloir_etage_1, "D": None}
        depot_affaire.exits = {"N": entree, "E": None, "S": None, "O": None,
                               "U": couloir_etage_1, "D": None}
        jardin.exits = {"N": cours_botanique, "E": entree, "S": None,
                        "O": None, "U": couloir_etage_1, "D": None}
        cours_botanique.exits = {"N": None, "E": None, "S": jardin, "O": None,
                                 "U": couloir_etage_1, "D": None}
        couloir_etage_1.exits = {"N": salle_commune_de_gryffondor,"E": cours_de_magie,
                                 "S": salle_commune, "O": None, "U": couloir_etage_2, "D": entree}
        salle_commune_de_gryffondor.exits = {"N": None, "E": None, "S": couloir_etage_1, "O": None,
                                             "U": couloir_etage_2, "D": entree}
        cours_de_magie.exits = {"N": None, "E": None, "S": None, "O": couloir_etage_1,
                                "U": couloir_etage_2, "D": entree}
        salle_commune.exits = {"N": couloir_etage_1, "E": None, "S": None, "O": None,
                               "U": couloir_etage_2, "D": entree}
        couloir_etage_2.exits = {"N": cours_potion, "E": salle_commune_serpentard,
                                 "S": toilette, "O": cours_animaux_magiques,
                                 "U": couloir_etage_3, "D": couloir_etage_1}
        cours_potion.exits = {"N": None, "E": None, "S": couloir_etage_2, "O": None,
                              "U": couloir_etage_3, "D": couloir_etage_1}
        salle_commune_serpentard.exits = {"N": None, "E": None, "S": None, "O": couloir_etage_2,
                                          "U": couloir_etage_3, "D": couloir_etage_1}
        cours_animaux_magiques.exits = {"N": None, "E": couloir_etage_2, "S": None, "O": None,
                                        "U": couloir_etage_3, "D": couloir_etage_1}
        toilette.exits = {"N": couloir_etage_2, "E": salle_sombre, "S": None, "O": None,
                          "U": couloir_etage_3, "D": couloir_etage_1}
        couloir_etage_3.exits = {"N": salle_commune_de_poufsouffle,
                                 "E": salle_commune_de_serdaigle, "S": cours_de_defense,
                                 "O": None, "U": None, "D": couloir_etage_2}
        salle_commune_de_poufsouffle.exits = {"N": None, "E": None,
                                              "S": couloir_etage_3, "O": None,
                                              "U": None, "D": couloir_etage_2}
        salle_commune_de_serdaigle.exits = {"N": None, "E": None, "S": None,
                                            "O": couloir_etage_3, "U": None,
                                            "D": couloir_etage_2}
        cours_de_defense.exits = {"N": couloir_etage_3, "E": None,
                                  "S": None, "O": None, "U": None,
                                  "D": couloir_etage_2}
        salle_sombre.exits = {"N": None, "E": None, "S": None, "O": toilette, "U": None, "D": None}

        # Setup items
        baguette = Item("baguette", "une baguette magique en écailles de dragon", 30)
        depot_affaire.inventory[baguette.name] = baguette
        cape = Item("cape", "une longue cape noire", 50)
        depot_affaire.inventory[cape.name] = cape
        chapeau = Item("chapeau", "un chapeau pointu légèrement abîmé", 60)
        depot_affaire.inventory[chapeau.name] = chapeau
        beamer = Beamer("beamer", "un appareil magique pour se téléporter.", 25)
        toilette.inventory[beamer.name] = beamer
        livre = Item("livre", "un livre de sorts", 10)
        potion = Item("potion", "une potion de guérison", 5)
        cape_sombre = Item("cape", "une cape noire avec des motifs plus sombres", 5)
        diplome_de_magie = Item("diplôme de magie", "un diplôme de magie", 1)
        diplome_de_botanique = Item("diplôme de botanique", "un diplôme de botanique", 1)
        diplome_de_potion = Item("diplôme de potion", "un diplôme de potion", 1)
        diplome_d_animaux_magiques = Item("diplôme d'animaux magiques",
                                          "un diplôme d'animaux magiques", 1)
        diplome_de_defense = Item("diplôme de défense", "un diplôme de défense", 1)

        # Setup characters (PNJ)
        chapeau_magique = Character(
            "chapeau_magique", 
            "un chapeau sombre et abîmé capable de parler", 
            salle_commune,
            [
                "Bonjour, je suis un chapeau magique.",
                "Je peux vous aider à choisir votre maison.",
                "Quelle maison voulez-vous rejoindre ?"
            ],
            can_move=False
        )
        salle_commune.characters[chapeau_magique.name] = chapeau_magique

        dumbledore = Character(
            "Dumbledore", 
            "le directeur de l'école", 
            salle_commune,
            [
                "Bienvenue à Poudlard !",
                "Abracadabra !",
                "Je suis Albus Dumbledore, le directeur de cette école.",
                "N'oubliez pas de toujours faire ce qui est juste."
            ],
            can_move=False
        )
        salle_commune.characters[dumbledore.name] = dumbledore

        hagrid = Character(
            "Hagrid", 
            "le gardien des clés et des lieux", 
            jardin,
            [
                "Salut, je suis Hagrid.",
                "Je m'occupe des créatures magiques.",
                "Avez-vous besoin d'aide pour nourrir les créatures ?"
            ],
            can_move=False
        )
        jardin.characters[hagrid.name] = hagrid

        professeur_de_magie = Character(
            "professeur_de_magie", 
            "le professeur de magie avec un très large chapeau", 
            cours_de_magie,
            [
                "Je suis le professeur de magie.",
                "Aujourd'hui, nous allons apprendre le sort 'Accio'.",
                "Répétez après moi : 'Accio'."
            ],
            can_move=False
        )
        cours_de_magie.characters[professeur_de_magie.name] = professeur_de_magie

        professeur_des_animaux_magiques = Character(
            "professeur_des_animaux_magiques", 
            "le professeur des animaux magiques avec un manteau vert", 
            cours_animaux_magiques,
            [
                "Je suis le professeur des animaux magiques.",
                "Aujourd'hui, nous allons étudier les hippogriffes.",
                "Répétez après moi : 'Hippogriffe'."
            ],
            can_move=False
        )
        cours_animaux_magiques.characters[professeur_des_animaux_magiques.name] = professeur_des_animaux_magiques

        professeur_de_botanique = Character(
            "professeur_de_botanique", 
            "le professeur de botanique avec des gants", 
            cours_botanique,
            [
                "Je suis le professeur de botanique.",
                "Aujourd'hui, nous allons replanter des mandragores.",
                "N'oubliez pas de mettre vos bouchons d'oreilles."
            ],
            can_move=False
        )
        cours_botanique.characters[professeur_de_botanique.name] = professeur_de_botanique

        professeur_de_potion = Character(
            "professeur_de_potion", 
            "le professeur de potions avec une longue cape sombre", 
            cours_potion,
            [
                "Je suis le professeur de potions.",
                "Aujourd'hui, nous allons préparer la potion Felix Felicis.",
                "Ajoutez des crochets d'araignée et des feuilles de mandragore."
            ],
            can_move=False
        )
        cours_potion.characters[professeur_de_potion.name] = professeur_de_potion

        professeur_de_defense = Character(
            "professeur_de_defense", 
            "le professeur de défense avec une longue cape", 
            cours_de_defense,
            [
                "Je suis le professeur de défense.",
                "Aujourd'hui, nous allons apprendre le sort 'Stupéfix'.",
                "Répétez après moi : 'Stupéfix'."
            ],
            can_move=False
        )
        cours_de_defense.characters[professeur_de_defense.name] = professeur_de_defense

        # Ajouter des étudiants
        harry = Character(
            "Harry_Potter", 
            "un étudiant célèbre avec une cicatrice en forme d'éclair", 
            salle_commune_de_gryffondor,
            [
                "Salut, je suis Harry Potter.",
                "Je suis en train de pratiquer des sorts."
            ],
            can_move=True
        )
        salle_commune_de_gryffondor.characters[harry.name] = harry

        hermione = Character(
            "Hermione Granger", 
            "une étudiante très intelligente", 
            salle_commune_de_gryffondor,
            [
                "Bonjour, je suis Hermione Granger.",
                "Je suis en train de lire un livre de sorts."
            ],
            can_move=True
        )
        salle_commune_de_gryffondor.characters[hermione.name] = hermione

        ron = Character(
            "Ron Weasley", 
            "un étudiant avec des cheveux roux", 
            salle_commune_de_gryffondor,
            [
                "Salut, je suis Ron Weasley.",
                "Je suis en train de jouer aux échecs sorciers."
            ],
            can_move=True
        )
        salle_commune_de_gryffondor.characters[ron.name] = ron

        draco = Character(
            "Draco Malfoy", 
            "un étudiant de Serpentard avec une attitude arrogante", 
            salle_commune_serpentard,
            [
                "Salut, je suis Draco Malfoy.",
                "Je suis en train de comploter quelque chose."
            ],
            can_move=True
        )
        salle_commune_serpentard.characters[draco.name] = draco

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = entree

        # Setup conditions
        self.conditions = Conditions(self)

        # Setup quests
        quest_steps = [
            QuestStep(
                "Parlez au chapeau dans la salle commune.",
                character=chapeau_magique,
                special_responses=[
                    ("chapeau magique : Bonjour, je suis ici"
                     " pour que vous choisissiez votre maison."),
                    "chapeau magique : Quelle maison voulez-vous ?"
                ],
                choices=[
                    ["Oui, je veux choisir.", "Non, je suis occupé."],
                    ["Gryffondor", "Serpentard", "Serdaigle", "Poufsouffle"]
                ],
                correct_choices=[["Oui, je veux choisir."],
                                ["Gryffondor", "Serpentard", "Serdaigle", "Poufsouffle"]],
                reward_item=cape_sombre
            ),
            QuestStep(
                "Assister au cours de magie dans la salle de magie.",
                character=professeur_de_magie,
                special_responses=[
                    ("professeur de magie : Bienvenue à Poudlard !"
                     " Êtes-vous prêt à apprendre un sort ?"),
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
                "Assister au cours de botanique dans la salle de botanique.",
                character=professeur_de_botanique,
                special_responses=[
                    ("professeur de botanique : Bienvenue à Poudlard !"
                     " Êtes-vous prêt à apprendre un sort ?"),
                    ("professeur de botanique : Pour replanter une mandragore, il faut"
                     " l'arracher d'un coup sec en mettant vos bouchons d'oreilles."),
                    ("professeur de botanique : Placez ensuite la mandragore"
                     " dans le nouveau pot et remblayez avec de la terre.")
                ],
                choices=[
                    ["Oui, je suis prêt.", "Non, pas maintenant."],
                    ["Arracher la plante",
                     "Mettre ses bouchons d'oreilles et arracher la plante",
                     "Mettre ses bouchons d'oreilles"],
                    ["Mettre la mandragore dans un pot et rajouter du fumier",
                     "Mettre la mandragore dans un pot",
                     "Mettre de la terre dans le pot"]
                ],
                correct_choices=[
                    ["Oui, je suis prêt."],
                    ["Mettre ses bouchons d'oreilles et arracher la plante"],
                    ["Mettre la mandragore dans un pot et rajouter du fumier"]
                ],
                reward_item=diplome_de_botanique
            ),
            QuestStep(
                "Assister au cours de potions dans la salle de potions.",
                character=professeur_de_potion,
                special_responses=[
                    ("professeur de potions : Bienvenue à Poudlard !"
                     " Êtes-vous prêt à apprendre un sort ?"),
                    ("professeur de potions : Pour faire du Felix "
                     "Felicis, mettez des crochets d'araignée."),
                    "professeur de potions : Ensuite, ajoutez des feuilles de mandragore."
                ],
                choices=[
                    ["Oui, je suis prêt.", "Non, pas maintenant."],
                    ["Mettre de l'eau",
                     "Mettre des crochets d'araignée",
                     "Mettre du jus de citrouille"],
                    ["Mettre des feuilles de mandragore",
                     "Mettre une plume de hibou",
                     "Mettre du radis venimeux"]
                ],
                correct_choices=[
                    ["Oui, je suis prêt."],
                    ["Mettre des crochets d'araignée"],
                    ["Mettre des feuilles de mandragore"]
                ],
                reward_item=diplome_de_potion
            ),
            QuestStep(
                "Assister au cours d'animaux magiques.",
                character=professeur_des_animaux_magiques,
                special_responses=[
                    ("professeur des animaux magiques : Bienvenue à Poudlard !"
                     " Êtes-vous prêt à apprendre un sort ?"),
                    ("professeur des animaux magiques : Repérez un animal magique ressemblant"
                     " à un cheval mais avec une corne sur la tête."),
                ],
                choices=[
                    ["Oui, je suis prêt.", "Non, pas maintenant."],
                    ["Un hippogriffe", "Une licorne", "Un phénix"]
                ],
                correct_choices=[
                    ["Oui, je suis prêt."],
                    ["Une licorne"]
                ],
                reward_item=diplome_d_animaux_magiques
            ),
            QuestStep(
                "Assister au cours de défense dans la salle de défense.",
                character=professeur_de_defense,
                special_responses=[
                    ("professeur de défense : Bienvenue à Poudlard !"
                     " Êtes-vous prêt à apprendre un sort ?"),
                    "professeur de défense : Répétez après moi : 'Stupéfix'.",
                    "professeur de défense : Répétez après moi : 'Protego'.",
                    "professeur de défense : Répétez après moi : 'Petrificus Totalus'."
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
                reward_item=diplome_de_defense
            ),
        ]
        main_quest = Quest("La quête principale",
                           "Accomplissez les tâches pour avancer dans l'histoire.",
                           quest_steps)
        self.quests.append(main_quest)

    # Play the game
    def play(self):
        """ Play the game. """
        self.setup()
        self.print_welcome()
        required_items = [self.quests[0].steps[i].reward_item.name for i in range(len(self.quests[0].steps))]
        # Loop until the game is finished
        while not self.finished:
            self.process_command(input("> "))
            end_message = self.conditions.check_conditions(required_items)
            if end_message:
                self.finished = True

    # Process the command entered by the player
    def process_command(self, command_string) -> None:
        """
        Process the command entered by the player.
        Args:
            command_string (str): The command entered by the player.
        """
        # Split the command string into a list of words
        list_of_words = command_string.split(" ")
        command_word = list_of_words[0]
        if command_word != "":
            # If the command is not recognized, print an error message
            if command_word not in self.commands:
                print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
            # If the command is recognized, execute it
            else:
                command = self.commands[command_word]
                command.action(self, list_of_words, command.number_of_parameters)
                if command_word != "quit":
                    self.move_characters()

    # Print the welcome message
    def print_welcome(self):
        """ Print the welcome message for the player. """
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
        """ Move the characters in the game. """
        for room in self.rooms:
            # Créer une copie de la liste des personnages dans la pièce
            characters_to_move = list(room.characters.values())  # Liste des personnages à déplacer
            for character in characters_to_move:
                character.move()

def main():
    """ Main function to run the game. """
    # Create a game object and play the game
    Game().play()

if __name__ == "__main__":
    main()
