from classes.mammal import Mammal

class Dog(Mammal):

    def __init__(self, name, is_good=True):
        super().__init__(name=name, is_alive=True, rested=True)
        self.is_good = is_good

    def good_boy(self):
        if self.is_good== True:
            return "good boy"     
        else:
            return "okay boy"
        
    def energy(self):
        if self.rested == True:
            return "ready to play"
        else:
            return "ready to take nappy"

    def __repr__(self):
        return f"{self.name} is a {self.good_boy()} and he is {self.energy()}"

    def make_sound(self):
        return "Bark bark bark"
    
    def sleep(self):
        super().sleep(rested = False)
        return "ZZzZZzZzzzzZZzZzZZ"

    def run_around(self):
        super().run_around(rested = True)
        print (f"{self.name} is running around")
