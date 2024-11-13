# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        
        # Setup rooms

        entrée = Room("entrée", "dans le couloire principale de l'ecole de poudlard.")
        self.rooms.append(entrée)
        depot_affaire = Room("dépôt affaire", "dans la pièce remplie d'affaires d'étudiants de l'école.")
        self.rooms.append(depot_affaire)
        jardin = Room("jardin", "dans un jardin, au milieu, il y a une fontaine avec des plantes qui chantent.")
        self.rooms.append(jardin)
        cours_botanique = Room("cours_botanique", "dans une serre entourée de plantes magiques.")
        self.rooms.append(cours_botanique)
        couloir_etage_1 = Room("couloir_etage_1", "dans le couloire de l'étage 1.")
        self.rooms.append(couloir_etage_1)
        salle_commune_de_Gryffondor = Room("salle_commune_de_Gryffondor", "dans la salle commune de Gryffondor, cette salle est remplie de rouge, avec principalement du bois comme matériau.")
        self.rooms.append(salle_commune_de_Gryffondor)
        cours_de_magie = Room("cours_de_magie", "dans une salle de classe avec plusieurs rangées de tables et une céramique de dinosaure au plafond.")
        self.rooms.append(cours_de_magie)
        salle_commune = Room("salle_commune", "dans une grande salle avec plusieurs tables de banquet, tout au bout de la salle il y a la table des professeurs, des bougies flottant au plafond.")
        self.rooms.append(salle_commune)
        couloir_etage_2 = Room("couloir_etage_2", "dans un couloir très large rempli de fenêtres avec une vue incontournable.")
        self.rooms.append(couloir_etage_2)
        cours_potion = Room("cours_potion", "dans une salle sombre avec plusieurs paillasses, possédant une marmite et des produits que vous ne connaissez pas.")
        self.rooms.append(cours_potion)
        salle_commune_Serpentard = Room("salle_commune_Serpentard", "dans une salle avec un aquarium, des canapés en cuir et à l'étage vos lits aux couleurs du blason.")
        self.rooms.append(salle_commune_Serpentard)
        toilette = Room("toilette", "dans une salle avec des robinets en plein milieu et un peu d'eau au sol.")
        self.rooms.append(toilette)
        cours_animaux_magiques = Room("cours_animaux_magiques", "dans une salle plusieurs animaux en cage, et des squelettes autour de la salle.")
        self.rooms.append(cours_animaux_magiques)
        couloir_etage_3 = Room("couloir_etage_3", "dans une tour avec un couloir très fin.")
        self.rooms.append(couloir_etage_3)
        salle_commune_de_Poufsouffle = Room("salle_commune_de_Poufsouffle", "dans une pièce ovale avec plusieurs étagères remplies de livres.")
        self.rooms.append(salle_commune_de_Poufsouffle)
        salle_commune_de_Serdaigle = Room("salle_commune_de_Serdaigle", "dans une très épurée, très claire et remplie de fenêtres qui laissent entrer la lumière du jour.")
        self.rooms.append(salle_commune_de_Serdaigle)
        cours_de_defance = Room("cours_de_defance", "dans une salle possédant un pupitre d'affrontement de sorciers et des chaises.")
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


        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = swamp

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
