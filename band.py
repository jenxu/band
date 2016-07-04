class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()
        
    def count(self):
        pass
        
class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
class Drummer(Musician):
    def __init__(self):
        super().__init__(["Boom", "Clack", "Tsss"])
    
    def count(self):
        print("One, Two, Three, Four")
    
    def combust(self):
        print("I just spontaneously combusted")
        
class Band(object):
    def __init__(self):
        self.members = []
        
    def hire(self, musician):
        self.members.append(musician)
        
    def fire(self, musician):
        self.members.remove(musician)
    
    def play_solos(self):
        for member in self.members:
            member.count()
        for member in self.members:        
            member.solo(3)
            
if __name__ == '__main__':
    bob = Guitarist()
    john = Bassist()
    steve = Drummer()
    coldplay = Band()
    coldplay.hire(john)
    coldplay.hire(steve)
    coldplay.hire(bob)
    coldplay.play_solos()
    coldplay.fire(john)
    coldplay.play_solos()
