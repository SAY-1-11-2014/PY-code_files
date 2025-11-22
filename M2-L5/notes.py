class PINGU:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print('The name of penguin is ', self.name)
        print('The age of penguin is ', self.age)
    
class TINGU(PINGU): #creation of child class
    def __init__(self, nature, surroundings, name, age):
        self.nature = nature
        self.surroundings = surroundings
        PINGU.__init__(self,name,age) #inherit 

    def display(self):
        print('The nature is ', self.nature)
        print('They are surrounded by ', self.surroundings)
        PINGU.display(self)

t1 = TINGU('Happy','Ice Caps','Tilu',25)
t1.display()