from random import randint
from player import Player
import sys
from commands import Commands 

def main(a):
    print ("(type help to get a list of actions)\n")
    print ("%s enters the school, searching for a teacher." % a)
    while(p.health > 0):
        line = input("> ")
        args = line.split()
        if len(args) > 0:
            commandFound = False
            for c in Commands.keys():
                if args[0] == c[:len(args[0])]:
                    Commands[c](p)
                    commandFound = True
                    break
            if not commandFound:
                print ("%s doesn't understand the suggestion. Bolna kya chahte ho?" % a)

if __name__ == "__main__":
    for i in range (3):
        p = Player()
        p.name = input("Bol tera naam kya hain?\n")
        p.name = str.capitalize(p.name)
        if len(p.name) != 0:
            main(p.name)
            break
        else:
            if i == 2:
                print("Maar ja tu!!!")
                sys.exit()
            elif i == 1:
                print("Fir se puuch raha hoon!!")
            else:
                print("Wapas puuch raha hoon!")
