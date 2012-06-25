class MenuItem:
    def __init__(self):
        self.name=""
        self.price=0
    def Show(self):
        print("%s       %i "%(self.name,self.price))

Spag=MenuItem()
Spag.name="Spaghetti"
Spag.price=95

Coke=MenuItem()
Coke.name="Coke"
Coke.price=25

Spag.Show()
Coke.Show()
