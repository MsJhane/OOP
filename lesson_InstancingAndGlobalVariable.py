class Score:
    def __init__(self):
        self.score=0
    def add(self):
        self.score+=1
    def Show(self):
        print("The score is: %i "  %
              (self.score))

Basketball=Score()
Volleyball=Score()
Chess=Score()

Basketball.add()
Basketball.add()
Basketball.add()
Basketball.add()
Basketball.add()
Basketball.add()
Basketball.add()
Basketball.add()
Basketball.add()
Basketball.add()


Volleyball.add()
Volleyball.add()
Volleyball.add()
Volleyball.add()
Volleyball.add()


Chess.add()
Chess.add()
Chess.add()

Basketball.Show()
Volleyball.Show()
Chess.Show()
