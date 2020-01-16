from model.connection import *
from view.messageView import *
import sys 



if __name__=='__main__':
    choix=""
    show=Messageview()
    show.index()

    while choix != "a" or choix != "r" or choix != "q":
        choix = input("(e) pour écrire un message (l) pour lire les messages et (q) pour quitter ..:").lower()
        choice = Lire() 
        
        if choix == "l":
            show.index()
        
        if choix == "e":
            nom = input("Veuillez entrer votre nom : ").lower()
            text = input("Veuillez entrer votre message: ").lower()
            choice.write(nom, text)

        if choix == "q":
            print("A bientôt.")
            sys.exit() 
        

