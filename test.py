from room import Room
from character import Character

forest = Room("Forest", "une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.")
gandalf = Character("Gandalf", "un magicien blanc", forest, ["Abracadabra !"])
print(gandalf)