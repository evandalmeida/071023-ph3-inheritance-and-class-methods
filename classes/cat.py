from classes.mammal import Mammal

class Cat(Mammal):
    
    def __init__(self, name, lives_remaining=9):
        super().__init__(name=name, is_alive=True, rested=True)
        self.lives_remaining = lives_remaining

    def __repr__(self):
        return f"Cat(name={self.name}, lives_remaining={self.lives_remaining})"
    
    def make_sound(self):
        return "MEOW"
    
    def sleep(self):
        super().sleep()
        return "Do not disturb"