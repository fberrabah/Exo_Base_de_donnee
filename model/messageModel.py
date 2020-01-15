from model.connection import * 
from view.messageView import *

class Lire():
    def __init__(self):
        self.choice = connection()
    
    def read(self):
        self.choice.initialize_connection()
        self.choice.cursor.execute("SELECT * FROM message;")
        test = self.choice.cursor.fetchall()
        self.choice.close_connection()
        return test

    def write(self, nom, text):
        self.choice.initialize_connection()
        self.choice.cursor.execute("INSERT INTO message(content, publishing_date, author) VALUES(%s, NOW(), %s)" ,(text, nom))
        self.choice.connection.commit()
        self.choice.close_connection()


