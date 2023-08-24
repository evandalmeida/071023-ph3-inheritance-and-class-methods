class Bird:

    number_of_birds = 0
    all_the_birds = []
    max_number_of_birds = 10

    def __init__(self, name, hungry= True):
        self.name = name
        Bird.number_of_birds += 1
        Bird.all_the_birds.append(self)
    
    def __repr__(self):
        return f"{self.name}"

    def tweet(self):
        return f"{self.name} is posting all their tweets"
    
    @classmethod
    def flock(cls):
        for bird in cls.all_the_birds:
            print(f"{bird.name} is flying")

    @classmethod
    def eat_tg(cls):
        for bird in cls.all_the_birds:
            bird.hungry =False
            print(f"{bird.name} gobble gobble")