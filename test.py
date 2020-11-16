class Person:
    def __init__(self, age, nom):
        self.nom = nom
        self.age = age

    def walking(self):
        print("walking")
    
moi = Person(21, "yves")
