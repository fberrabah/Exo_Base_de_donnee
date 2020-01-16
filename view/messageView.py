from model.messageModel import *

class Messageview():
 
    def __init__(self):
        self.model = Lire()
        

    def index(self):
        """Display all messages from the database"""
        # get the messages from the model
        messages = self.model.read()
        print('Bonjour et bienvenue sur le forum, voici les derniers messages : ')
        if messages:
            for message in messages:
                print("\nmessage {} : {}".format(message['id'], message['content']))
                print("Posté par {} le {} à {}".format(
                message['author'],
                message['publishing_date'].strftime("%d/%m/%Y"),
                message['publishing_date'].strftime("%H:%M")
                ))
                print("\n------------------------------")
        else:
            print("Aucun message pour le moment")

