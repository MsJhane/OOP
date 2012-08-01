class Clock:
    def Time(self):
        print("clock says 6:00")

class WallClock(Clock):
    def Time(self):
        print("The wall clock says 6:00")

class WristWatch(Clock):
    def Time(self):
        print("The wrist watch says 6:00")

class Rolex(WristWatch):
    def Time(self):
        print("The expensive rolex says 6:00")

class FakeRolex(Rolex):
    def Time(self):
        Clock.Time(self)
        
    
        
watch=FakeRolex()
watch.Time()

